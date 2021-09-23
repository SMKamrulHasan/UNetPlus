
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

![Sub-TernausNet (3)](https://user-images.githubusercontent.com/42282006/63461920-b15de480-c427-11e9-804a-30c849d19f8c.png)

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




<!DOCTYPE html>
<html>

<head lang="en">
    <meta charset="UTF-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">

    <title>L-CO-Net</title>

    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="icon" type="image/png" href="img/seal_icon.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.8.0/codemirror.min.css">
    <link rel="stylesheet" href="css/app.css">
    <link rel="stylesheet" href="css/bootstrap.min.css">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.8.0/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.5.3/clipboard.min.js"></script>
    <script src="js/app.js"></script>
</head>

<body>
<div class="container" id="main">
    <div class="row">

        <h2 class="col-md-12 text-center" style="padding-bottom:20px">

            <b>L-CO-Net: Learned Condensation-Optimization Network for Clinical Parameter Estimation from Cardiac Cine MRI</br></b>
            <span style="font-size:18pt"> EMBC 2020, Oral </span>
            <br>
        </h2>

    </div>
    <div class="row">
        <div class="col-md-12 text-center">
            <ul class="list-inline" style="font-size:18pt">
                <li>
                    <a href="http://ai.stanford.edu/~optas/">
                        S. M. Kamrul Hasan
                    </a>
                    </br>Rochester Institute of Technology
                </li>
                <li>
                    <a href="http://aabdelreheem.me">
                        Cristian A. Linte
                    </a>
                    </br>Rochester Institute of Technology
                </li>
            </ul>
        </div>
    </div>


    <div class="row" style="padding-top:45px">
        <div class="col-md-6 col-md-offset-3 text-center">
            <ul class="nav nav-pills nav-justified">
                <li>
                    <a href="https://arxiv.org/abs/2004.11253">
                        <h4><strong>[ Paper ]</strong></h4>
                    </a>
                </li>
                <li>
                    <a href="#video">
                        <h4><strong>[ Video ]</strong></h4>
                    </a>
                </li>
                <li>
                    <a href="https://github.com/lconet">
                        <h4><strong>[ Code ]</strong></h4>
                    </a>
                </li>
                <li>
                    <a href="#dataset">
                        <h4><strong>[ Dataset ]</strong></h4>
                    </a>
                </li>
            </ul>
        </div>
    </div>


    <div class="row" style="padding-bottom:30px">
        <div class="col-md-8 col-md-offset-2">
            <h3>
                <b>Abstract</b>
            </h3>
            <p class="text-justify">
                In this work, we implement a fully convolutional segmenter featuring both a learned group structure and a regularized weight-pruner to reduce the high computational cost in volumetric image segmentation. We validated our framework on the ACDC dataset featuring one healthy and four pathology groups imaged throughout the cardiac cycle. Our technique achieved Dice scores of 96.8% (LV blood-pool), 93.3% (RV blood-pool) and 90.0% (LV Myocardium) with five-fold cross-validation and yielded similar clinical parameters as those estimated from the ground truth segmentation data. Based on these results, this technique has the potential to become an efficient and competitive cardiac image segmentation tool that may be used for cardiac computer-aided diagnosis, planning, and guidance applications.
            </p>
        </div>
    </div>


    <div class="row" id="video" style="padding-bottom:30px">
        <div class="col-md-8 col-md-offset-2">
            <h3>
                <b>Video</b>
            </h3>
            <video id="v0" width="100%" loop="" muted="" controls="">-->
                <source src="img/hi_res.mp4" type="video/mp4">-->
           </video>
        </div>

    </div>

    <div class="row" id="dataset" style="padding-bottom:30px">
        <div class="col-md-8 col-md-offset-2">
            <h3>
                <b>Dataset</b>
            </h3>
           For this study, we used the ACDC dataset, which is composed of short-axis cardiac cine-MR images acquired from 100 different patients divided into 5 evenly distributed subgroups according to their cardiac condition: normal- NOR, myocardial infarction- MINF, dilated cardiomyopathy- DCM, hypertrophic cardiomyopathyHCM, and abnormal right ventricle- ARV, available as a part of the STACOM 2017 ACDC challenge.</a>.
            <br>
        </div>
    </div>

    <div class="row" style="padding-bottom:30px">
        <div class="col-md-8 col-md-offset-2">
            <h3>
                <b>Method: L-CO-Net</b>
            </h3>
        </div>

        <div class="col-md-8 col-md-offset-2">
            <figure>
                <img src="img/method.png" style="padding-bottom:10px" class="img-responsive" alt="overview">
                    <figcaption>
                    </figcaption>
            </figure>
        </div>

        <div class="col-md-8 col-md-offset-2">
            Illustration of L-CO-Net framework: (a) ROI detection around LV-RV; (b) Segmentation block consisting of a decoder and an
encoder where each condense block (CB) consists of 3 Layers with a growth rate of k = 16. The transformations within each CB and the
transition-down block are labeled with a cyan and yellow box, respectively.
        </div>
    </div>


    <div class="row" style="padding-bottom:30px">
        <div class="col-md-8 col-md-offset-2">
            <h3>
                <b>Qualitative Results</b>
            </h3>
        </div>

        <div class="col-md-8 col-md-offset-2">
            <figure>
                <img src="img/listener_qualitative_res.png" style="padding-bottom:10px" class="img-responsive" alt="overview">
                <figcaption>
                </figcaption>
            </figure>
        </div>

        <div class="col-md-8 col-md-offset-2">
            Representative ED and ES frames segmentation results of a complete cardiac cycle from the base (high slice index) to apex (low
slice index) showing RV blood-pool, LV blood-pool, and LV-Myocardium in purple, red, and cyan respectively
        </div>
    </div>

    <div class="row" id="citation" style="padding-bottom:30px">
        <div class="col-md-8 col-md-offset-2">
            <h3>
                <b>Citation</b>
            </h3>
            If you find our work useful in your research, please consider citing:
<pre class="w3-panel w3-leftbar w3-light-grey">
@inproceedings{hasan2020co,
  title={L-CO-Net: Learned Condensation-Optimization Network for Segmentation and Clinical Parameter Estimation from Cardiac Cine MRI},
  author={Hasan, SM Kamrul and Linte, Cristian A},
  booktitle={2020 42nd Annual International Conference of the IEEE Engineering in Medicine \& Biology Society (EMBC)},
  pages={1217--1220},
  year={2020},
  organization={IEEE}
}</pre>
        </div>
    </div>

    <div class="row" id="benchmark" style="padding-bottom:30px">
        <div class="col-md-8 col-md-offset-2">
            <h3>
                <b>L-CO-Net participated post MICCAI STACOM-2017 ACDC Challenge</b>
            </h3>
            Coming soon!
        </div>

    </div>


    <div class="row" style="padding-bottom:30px">
        <div class="col-md-8 col-md-offset-2">
            <h3>
                <b>Acknowledgements</b>
            </h3>
            <p class="text-justify">
                Research reported in this publication was supported by the National Institute of General Medical Sciences of the National Institutes of Health
under Award No. R35GM128877 and by the Office of Advanced Cyber infrastructure of the National Science Foundation under Award No.
1808530. </a>.
            </p>
        </div>
    </div>


    </div>
        <script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=080808&w=110&t=tt&d=_kJ7hJdlh3UTdIJueDububmhQbOOTRZpo-A1RUHuEqU&co=ffffff&cmo=3acc3a&cmn=ff5353&ct=808080'></script>
    </body>

</html>
