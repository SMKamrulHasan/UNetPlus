
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

QUANTITATIVE EVALUATION OF THE SEGMENTATION RESULTS. MEAN AND (STANDARD DEVIATION) VALUES ARE REPORTED FOR IOU(%) AND DICE
COEFFICIENT(%) FROM ALL NETWORKS AGAINST THE PROVIDED REFERENCE SEGMENTATION. THE STATISTICAL SIGNIFICANCE OF THE RESULTS FOR
U-NET + NN AND U-NETPLUS MODEL COMPARED AGAINST THE BASELINE MODEL (U-NET AND TERNASUNET) ARE REPRESENTED BY ∗ AND ∗∗ FOR
P-VALUES 0.1 AND 0.05, RESPECTIVELY. U-NET HAS BEEN COMPARED WITH U-NET+NN, TERNAUSNET HAS BEEN COMPARED WITH U-NETPLUS. THE
BEST PERFORMANCE METRIC (IOU AND DICE) IN EACH CATEGORY (BINARY, INSTRUMENT PART AND INSTRUMENT TYPE SEGMENTATION) IS
INDICATED IN BOLD TEXT.

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

