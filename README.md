# Dynamic_Mapping on Settlement Hierarchy Analysis 
This project analyzes population distribution across settlements in the **Eastern Province of Sri Lanka**, applying **harmonized ranking methods** and the **Rank-Size Rule** to better understand settlement hierarchy over time. The results are visualized through dynamic maps.
![Settlement](https://github.com/user-attachments/assets/26ee2fb3-6f99-41ca-802f-a21dc1069f44)

## Project Overview
Settlement hierarchy refers to the organization of human settlements in a region based on population size. Traditional ranking methods (e.g., Rank 1 = highest population) may distort relationships due to irregular gaps between settlement sizes. To address this, we use the **Rank-Size Rule**:

<img width="337" height="196" alt="image" src="https://github.com/user-attachments/assets/cfa8ac3d-33f3-41cc-a2ab-5c9326208c84" />


This rule helps understand the relative position of settlements in a more proportionate and analytical manner. In this study, **45 settlements** were identified across the Eastern Province and assessed for the years **2012, 2015, 2018, and 2021**.


## Tools & Libraries

- `pandas` – Handling tabular population data  
- `geopandas` – Spatial join with shapefile  
- `matplotlib` – Map rendering  
- `mapclassify` – Custom bin classification  
- `Pillow (PIL)` – GIF creation  
- `matplotlib_scalebar` – Scale bar addition  
- `geemap.cartoee` – North arrow drawing  
- `glob` and `io` – Image sequencing and temporary memory handling






