import pandas as pd
import geopandas as gpd
import mapclassify
import PIL
import io
import glob
from PIL import Image
import matplotlib.pyplot as plt
from geemap import cartoee
from matplotlib_scalebar.scalebar import ScaleBar
import contextily as ctx

data = pd.read_csv('E:\Lavi\Semi-7\WebGIS\East_D.csv')

gnd=gpd.read_file("E:\Lavi\Semi-7\WebGIS\Eastern_D.shp")

for year in ['2012', '2015', '2018','2021']:
    merge = gnd.merge(data, on = 'DSD_N', how = 'right')

    size_scale = [240, 160, 120, 100, 70, 40]
    colors=['#63050d','#a50f15','#de2d26','#fb6a4a','#fc9272','#fcbba1' ]

    ax = merge.plot(figsize = (10,10), color='palegoldenrod',edgecolor='black', linewidth = 0.15)
    ax.set_facecolor('#e5e5e5')
    ctx.add_basemap(ax, crs=merge.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik,zoom=8)

    for index, row in merge.iterrows():
        label = row[year]
        size = size_scale[int(label)-1]
        color = colors[int(label)-1]
        ax.scatter(row.geometry.centroid.x, row.geometry.centroid.y, s=size, color=color, edgecolor='black', linewidth=0.15)

    legend_handles=[]
    for i in range(len(size_scale)):
        label = "Rank "+str(i+1)
        size = size_scale[i]
        color=colors[i]
        legend_handles.append(ax.scatter([],[], s=size,color=color,edgecolor='black', label=label, linewidth = 0.15))

    leg=ax.legend(handles=legend_handles,ncol=2, prop={'size': 9.5}, frameon=True, bbox_to_anchor=(0.002, 0.013), loc='lower left')
    leg.set_title('Rank of Settlements',prop={'size':11})

    ax.add_artist(ScaleBar(1, dimension= 'si-length', units='m', location= 'lower right'))

    ax.set_title(f'Settlement Hierarchy- Eastern Province {year}', fontdict={'fontsize':26},fontweight='semibold',pad=15)
    ax.set_axis_on()
    cartoee.add_north_arrow(ax, text="N", xy=(0.95, 0.97), arrow_length=(0.1), text_color="Black", arrow_color="Black", fontsize=14)

    ax.set_xlim(150000, 350000)
    ax.set_ylim(130000, 450000)
    ax.tick_params(axis='both', labelsize=6)
    plt.savefig(f'Settlement{year}.png')


fp_in='Settlement*.png'
fp_out = "E:\Assign-02\Settlement.gif"

img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs, save_all=True, duration=500,loop=0)
