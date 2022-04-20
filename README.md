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

<details>  
<summary>Restoration...</summary>  
| Restoration tasks   |    Restored images   |
| ------------------- | :----------: |
| Denoise (real-world)|<img src="https://media.giphy.com/media/IEQGj4WRLxsbHvayGY/giphy.gif" alt="noise2" width="200" style="zoom:100%;" />|
| Derain (rainstreak) |<img src="https://media.giphy.com/media/SObtoc6A5Te0gI6RXt/giphy.gif" alt="rain" width="200" style="zoom:100%;" />|
| Derain (raindrop)   |<img src="https://media.giphy.com/media/yJJJkjMsfLMdRl7CN1/giphy.gif" alt="rain2" width="200" style="zoom:100%;" />|
| Dehaze (densehaze)  |<img src="https://media.giphy.com/media/YwbHdQ241UkY1U7tvN/giphy.gif" alt="haze" width="200" style="zoom:100%;" />|
| Deblur (motionblur) |<img src="https://media.giphy.com/media/DtxWtxJriS6mccMbZI/giphy.gif" alt="blur" width="200" style="zoom:100%;" />|
| LLEnhancement       |<img src="https://media.giphy.com/media/RkX38YYf8eFdMQ4L8I/giphy.gif" alt="ll" width="200" style="zoom:100%;" />|
| Retouching          |<img src="https://media.giphy.com/media/IFcyeXyXyuN3zbuOuD/giphy.gif" alt="rt" width="200" style="zoom:100%;" />|
</details>  

<details>  
<summary>Segmentation...</summary>
| Restoration tasks   |    Restored images   |
| ------------------- | :----------: |
| Instance segmentation|<img src="https://media.giphy.com/media/nNByZuGBET3u2u3MXr/giphy.gif" alt="noise2" width="200" style="zoom:100%;" />|
</details>  


