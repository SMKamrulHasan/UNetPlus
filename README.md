
# UNetPlus 
Pytorch implementation of our modified encoder-decoder framework

This repository contains code to train state-of-the-art surgical instruments segmentation networks as described in this paper:
U-NetPlus: A Modified Encoder-Decoder U-Net Architecture for Semantic and Instance Segmentation of Surgical Instrument. This architecture is trained on [MICCAI EndoVIs 2017 sub-challenge.](https://endovissub2017-roboticinstrumentsegmentation.grand-challenge.org)

In this work, we modify the U-Net architecture named UNetPlus, by introducing a pre-trained encoder and re-design the decoder part, by replacing the transposed convolution operation with an upsampling operation based on nearest-neighbor (NN) interpolation. To further improve performance, we also employ a very fast and flexible data augmentation technique. We trained
the framework on 8 × 225 frame sequences of robotic surgical videos, available through the MICCAI 2017 EndoVis Challenge
dataset and tested it on 8 × 75 frame and 2 × 300 frame videos. Using our U-NetPlus architecture, we report a 90.20%
DICE for binary segmentation, 76.26% DICE for instrument part segmentation, and 46.07% for instrument type (i.e., all instruments) segmentation, outperforming the results of previous techniques implemented and tested on these data.


# Prerequisites
Our code is compatible with python 3.7 or onward.

We depend on some python packages which need to be installed by the user:

* PyTorch
* tqdm
* SimpleITK
* sklearn
* numpy

# Authors 
* S. M. Kamrul Hasan ([sh3190@rit.edu])()
* Cristian A. Linte

# Contents 

* [Data]()
* [Method]()
* [Results]()
* [How to Run]()



# [Data]()

For both training and validation, we used the Robotic instruments dataset from the sub-challenge of MICCAI 2017
Endoscopic Vision Challenge [22]. The training dataset has 8 × 225 frame sequences with 2 Hz frame rate of high resolution stereo camera images collected from a da Vinci Xi surgical system during laparoscopic cholecystectomy procedures. The frames were re-sampled from 30 Hz video to 2 Hz to avoid any redundancy issues. A stereo camera was used to capture the video sequences that consists of the left and right eye views with resolution of 1920 × 1080 in RGB format. In each frame, the articulated parts of the robotic surgical instrument consisting of a rigid shaft, an articulated wrist, and claspers, have been manually labeled by expert clinicians. The test set has 8×75 frame sequences and 2×300 frame videos. The challenge is to segment 7 classes such as prograsp forceps, needle driver, vessel sealer, grasping retractor etc.

# [Method]()

U-NetPlus has an encoder network and a corresponding decoder network, followed by a final pixel-wise segmentation layer.

<div class="col-md-8 col-md-offset-2">
    <figure>
        <img src="https://user-images.githubusercontent.com/42282006/63461920-b15de480-c427-11e9-804a-30c849d19f8c.png" style="padding-bottom:1px" class="img-responsive" alt="overview">
            <figcaption>
            </figcaption>
    </figure>
</div>

<div class="col-md-8 col-md-offset-2">
    Illustration of L-CO-Net framework: (a) ROI detection around LV-RV; (b) Segmentation block consisting of a decoder and an
encoder where each condense block (CB) consists of 3 Layers with a growth rate of k = 16. The transformations within each CB and the
transition-down block are labeled with a cyan and yellow box, respectively.
</div>

        


# [Results]()

We compare our proposed architecture with three other models: U-Net, U-Net+NN, TernausNet. We can observe from this figure that after adding nearest-neighbor (NN) in the decoder of U-Net, the training accuracy of the classical U-Net framework (shown in blue) featuring the transposed convolution in the decodes, improves. Furthermore, the training of our proposed method (U-NetPlus) also converges faster and yields better training accuracy compared to TernausNet (shown in cyan). Hence, this graph alone illustrates the benefit of the nearest-neighbor interpolation on the segmentation performance.

# [Table]()


# [How to Run]()

# [Preprocessing]()

# [Train]()




 If you find our work useful in your research, please consider citing:
<pre class="w3-panel w3-leftbar w3-light-grey">
@inproceedings{hasan2019u,
  title={U-NetPlus: A modified encoder-decoder U-Net architecture for semantic and instance segmentation of surgical instruments from laparoscopic images},
  author={Hasan, SM Kamrul and Linte, Cristian A},
  booktitle={2019 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)},
  pages={7205--7211},
  year={2019},
  organization={IEEE}
}</pre>


# Note
Contact: S. M. Kamrul Hasan (smkamrulhasan.rit@gmail.com)





**L-CO-Net: Learned Condensation-Optimization Network for Clinical Parameter Estimation from Cardiac Cine MRI** EMBC 2020, Oral \
 {.col-md-12 .text-center style="padding-bottom:20px"}
---------------------------------------------------------------------------------------------------------------------------------

-   [S. M. Kamrul Hasan](http://ai.stanford.edu/~optas/) Rochester
    Institute of Technology
-   [Cristian A. Linte](http://aabdelreheem.me) Rochester Institute of
    Technology

-   [](https://arxiv.org/abs/2004.11253)

    #### **[ Paper ]**

-   [](#video)

    #### **[ Video ]**

-   [](https://github.com/lconet)

    #### **[ Code ]**

-   [](#dataset)

    #### **[ Dataset ]**

### **Abstract**

In this work, we implement a fully convolutional segmenter featuring
both a learned group structure and a regularized weight-pruner to reduce
the high computational cost in volumetric image segmentation. We
validated our framework on the ACDC dataset featuring one healthy and
four pathology groups imaged throughout the cardiac cycle. Our technique
achieved Dice scores of 96.8% (LV blood-pool), 93.3% (RV blood-pool) and
90.0% (LV Myocardium) with five-fold cross-validation and yielded
similar clinical parameters as those estimated from the ground truth
segmentation data. Based on these results, this technique has the
potential to become an efficient and competitive cardiac image
segmentation tool that may be used for cardiac computer-aided diagnosis,
planning, and guidance applications.

### **Video**

--\> --\>

### **Dataset**

For this study, we used the ACDC dataset, which is composed of
short-axis cardiac cine-MR images acquired from 100 different patients
divided into 5 evenly distributed subgroups according to their cardiac
condition: normal- NOR, myocardial infarction- MINF, dilated
cardiomyopathy- DCM, hypertrophic cardiomyopathyHCM, and abnormal right
ventricle- ARV, available as a part of the STACOM 2017 ACDC challenge..
\

### **Method: L-CO-Net**

![overview](img/method.png)

Illustration of L-CO-Net framework: (a) ROI detection around LV-RV; (b)
Segmentation block consisting of a decoder and an encoder where each
condense block (CB) consists of 3 Layers with a growth rate of k = 16.
The transformations within each CB and the transition-down block are
labeled with a cyan and yellow box, respectively.

### **Qualitative Results**

![overview](img/listener_qualitative_res.png)

Representative ED and ES frames segmentation results of a complete
cardiac cycle from the base (high slice index) to apex (low slice index)
showing RV blood-pool, LV blood-pool, and LV-Myocardium in purple, red,
and cyan respectively

### **Citation**

If you find our work useful in your research, please consider citing:

``` {.w3-panel .w3-leftbar .w3-light-grey}
@inproceedings{hasan2020co,
  title={L-CO-Net: Learned Condensation-Optimization Network for Segmentation and Clinical Parameter Estimation from Cardiac Cine MRI},
  author={Hasan, SM Kamrul and Linte, Cristian A},
  booktitle={2020 42nd Annual International Conference of the IEEE Engineering in Medicine \& Biology Society (EMBC)},
  pages={1217--1220},
  year={2020},
  organization={IEEE}
}
```

### **L-CO-Net participated post MICCAI STACOM-2017 ACDC Challenge**

Coming soon!

### **Acknowledgements**

Research reported in this publication was supported by the National
Institute of General Medical Sciences of the National Institutes of
Health under Award No. R35GM128877 and by the Office of Advanced Cyber
infrastructure of the National Science Foundation under Award No.
1808530. .
