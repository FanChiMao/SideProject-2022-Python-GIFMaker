# SideProject-2022-Python-GIFMaker  

## 1. Preparation  
You have two before/after images with the same size.

## 2. Run  
Place the restored image and noised image into specific folder, respectively.
Before running the `gif_maker.py`, you can adjust the following parameters:

```
--frame_dir   : the folder of being generated essential frames
--resize_scale: if image is too larger, you can consider to resize 
--step        : each frame with [step] pixels
--type:       : png or jpg or others
--frequency   : spending seconds in single loop
--repeat_GIF  : 0: repeat, 1: no repeat
--result_dir  : path of result gif 
```


## 3. Final examples  

- Restoration:  

  | Restoration task |    Restored images   |  Ground Truth     |
  | ---------------- | :----------: | :----------: |
  | Deraindrop       |<img src="https://media.giphy.com/media/nNByZuGBET3u2u3MXr/giphy.gif" alt="arch" width="300" style="zoom:100%;" />|<img src="https://i.imgur.com/fzfTRYQ.gif" alt="arch" width="300" style="zoom:100%;" />|
  | Dehaze           |<img src="figures/47.gif" alt="arch" width="300" style="zoom:100%;" />|<img src="figures/47_gt.png" alt="arch" width="300" style="zoom:100%;" />| 
  

- Deblur ([GoPro dataset](https://seungjunnah.github.io/Datasets/gopro)):  

  | Video restoration|    Restored images   |  
  | ---------------- | :----------: |  
  | Orginal       |<img src="figures/GoPro_1.gif" width="620" style="zoom:100%;" />|  
  | Deblur result |<img src="figures/GoPro_deblur.gif" width="620" style="zoom:100%;" />|  
