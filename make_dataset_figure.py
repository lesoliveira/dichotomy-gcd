"""Dataset examples figure (Omniglot, CUB-200-2011 and four UCR datasets).

    python make_dataset_figure.py   -> figures/datasets.pdf
"""
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
from pathlib import Path
from PIL import Image
plt.rcParams.update({"font.size":8.5,"font.family":"serif","pdf.fonttype":42,
                     "axes.spines.top":False,"axes.spines.right":False})
B,O="#2a78d6","#eb6834"
R=Path("data/omniglot"); U=Path(".")  # run get_omniglot.py and features_ts.py first
rng=np.random.default_rng(3)
def chars(part, alphas, idx):
    out=[]
    for a in alphas:
        cs=sorted((R/part/a).iterdir())
        for i in idx: out.append(sorted(cs[i].glob("*.png")))
    return out
known=chars("images_background",["Latin","Greek","Bengali"],[0,1])
near =chars("images_background",["Latin","Greek","Bengali"],[5,8])
far  =chars("images_evaluation",["Atlantean","Glagolitic","Tibetan"],[0,3])

CUBR=Path("data/CUB_200_2011/images")  # downloaded by features_cub.py
def birds(names): return [sorted((CUBR/n).glob("*.jpg"))[0] for n in names]
cub_known=birds(["001.Black_footed_Albatross","013.Bobolink","041.Scissor_tailed_Flycatcher","095.Baltimore_Oriole","151.Black_capped_Vireo","191.Red_headed_Woodpecker"])
cub_near=birds(["004.Groove_billed_Ani","025.Pelagic_Cormorant","060.Glaucous_winged_Gull","105.Whip_poor_Will","129.Song_Sparrow","157.Yellow_throated_Vireo"])
cub_far=birds(["002.Laysan_Albatross","034.Gray_crowned_Rosy_Finch","069.Rufous_Hummingbird","101.White_Pelican","149.Brown_Thrasher","183.Northern_Waterthrush"])
def montage_rgb(files, t=110, pad=6):
    W=len(files)*t+(len(files)+1)*pad; M=np.full((t+2*pad,W,3),255,np.uint8)
    for j,f in enumerate(files):
        im=Image.open(f).convert("RGB"); w,h=im.size; s=min(w,h)
        im=im.crop(((w-s)//2,(h-s)//2,(w-s)//2+s,(h-s)//2+s)).resize((t,t),Image.BICUBIC)
        M[pad:pad+t,pad+j*(t+pad):pad+j*(t+pad)+t]=np.asarray(im)
    return M
def montage(group, pad=6):
    t=105; H=2*t+3*pad; W=len(group)*t+(len(group)+1)*pad
    M=np.full((H,W),255,np.uint8)
    for j,files in enumerate(group):
        for r in range(2):
            im=np.array(Image.open(files[r*3]).convert("L"))
            y0=pad+r*(t+pad); x0=pad+j*(t+pad)
            M[y0:y0+t,x0:x0+t]=im
            M[y0,x0:x0+t]=200; M[y0+t-1,x0:x0+t]=200; M[y0:y0+t,x0]=200; M[y0:y0+t,x0+t-1]=200
    return M
fig=plt.figure(figsize=(7.2,4.5))
sf=fig.subfigures(3,1,height_ratios=[0.72,0.5,1.45],hspace=0.02)
sf[0].suptitle("(a) Omniglot, six characters per group, two drawings each",x=0.01,ha="left",fontsize=9.5,weight="bold")
ax=sf[0].subplots(1,3,gridspec_kw=dict(wspace=0.06))
for a_,(title,group) in zip(ax,[("Known (background alphabets)",known),("Near novel (same alphabets)",near),("Far novel (unseen alphabets)",far)]):
    a_.imshow(montage(group),cmap="gray",vmin=0,vmax=255); a_.set_title(title,fontsize=8,pad=3)
sf[1].suptitle("(b) CUB-200-2011, one image per species",x=0.01,ha="left",fontsize=9.5,weight="bold")
ax2=sf[1].subplots(1,3,gridspec_kw=dict(wspace=0.06))
for a_,(title,files) in zip(ax2,[("Known (SSB known classes)",cub_known),("Near novel (SSB Hard)",cub_near),("Far novel (SSB Easy)",cub_far)]):
    a_.imshow(montage_rgb(files)); a_.set_title(title,fontsize=8,pad=3)
for a_ in list(ax)+list(ax2):
    a_.set_xticks([]); a_.set_yticks([]); [sp.set_visible(False) for sp in a_.spines.values()]
sf[2].suptitle("(c) UCR time series, two classes per dataset, three series each",x=0.01,ha="left",fontsize=9.5,weight="bold")
ax3=sf[2].subplots(1,4,gridspec_kw=dict(wspace=0.32))
for ax_,(f,name) in zip(ax3,[("ts_ShapesAll","ShapesAll"),("ts_NonInvasiveFetalECGThorax1","Fetal ECG"),("ts_Crop","Crop"),("ts_SwedishLeaf","SwedishLeaf")]):
    d=np.load(U/f"{f}.npz",allow_pickle=True); S,y=d["series"],d["y"]
    cls=np.unique(y); c1,c2=cls[0],cls[len(cls)//2]
    for c,col in [(c1,B),(c2,O)]:
        for i in rng.choice(np.where(y==c)[0],3,replace=False):
            ax_.plot(S[i],color=col,lw=.8,alpha=.85)
    ax_.set_title(f"{name}\n{len(cls)} classes, length {S.shape[1]}",fontsize=8)
    ax_.tick_params(labelsize=7); ax_.set_xlabel("time step",fontsize=7.5); ax_.grid(axis="y",color="#e6e5e0",lw=.6)
sf[2].subplots_adjust(bottom=0.2,top=0.78)
Path("figures").mkdir(exist_ok=True)
fig.savefig("figures/datasets.pdf",bbox_inches="tight")
