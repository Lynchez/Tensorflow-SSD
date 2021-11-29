# Single Shot MultiBox Detector

Tensorflow SSD implementation from scratch. 

It's implemented and tested with **tensorflow 2.0, 2.1, and 2.2**

## Usage

There are five different backbone, 
    **Mobilenet_v2**
    **DenseNet121**
    **VGG16**
    **VGG19**
    **EfficientNetB1**.

You can easily specify the backbone to be used with the **--backbone** parameter.

To train and test SSD model:

```sh
python trainer.py --backbone "choose a backbone"
python predictor.py --backbone "choose a backbone"
```

If you have GPU issues you can use **-handle-gpu** flag with these commands:

```sh
python trainer.py -handle-gpu
```

## Sample output :

![](examples/test.jpeg)

## Writing TFlite Soon

## Custom Dataset Train Soon

## Easy Colab Trainer Soon