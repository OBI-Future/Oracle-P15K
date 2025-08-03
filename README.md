<div align="center">
<div>
<a href="https://github.com/OBI-Future/Oracle-P15K"><img src="https://visitor-badge.laobi.icu/badge?page_id=OBI-Future/Oracle-P15K"/></a>
    <a href="https://github.com/OBI-Future/Oracle-P15K"><img src="https://img.shields.io/github/stars/OBI-Future/Oracle-P15K"/></a>
    <a href="https://arxiv.org/abs/2504.09555"><img src="https://img.shields.io/badge/Arxiv-2504.09555-yellow"/></a>
    <a href="https://github.com/OBI-Future/Oracle-P15K"><img src="https://img.shields.io/badge/Awesome-Oracle--P15K-green"/></a>
</div>

<h1>Mitigating Long-tail Distribution in Oracle Bone Inscriptions: Dataset, Model, and Benchmark ☯️</h1>

_The first attempt to apply diffusion model in realistic and controllable OBI generation_

<div>
    <a href="https://cs.ecnu.edu.cn" target="_blank">Jinhao Li</a><sup>1*</sup>,
    <a href="https://scholar.google.com.hk/citations?hl=zh-CN&user=NSR4UkMAAAAJ" target="_blank">Zijian Chen</a><sup>2*</sup>,
    <a href="https://shss.sjtu.edu.cn" target="_blank">Runze Jiang</a><sup>3</sup>,
    <a href="https://shss.sjtu.edu.cn/Web/FacultyDetail/46?f=1&t=4" target="_blank">Tingzhu Chen</a><sup>3&dagger;</sup>,
    <a href="https://faculty.ecnu.edu.cn/_s16/wzb/main.psp" target="_blank">Changbo Wang</a><sup>1&dagger;</sup>,
    <a href="https://scholar.google.com.hk/citations?hl=zh-CN&user=E6zbSYgAAAAJ" target="_blank">Guangtao Zhai</a><sup>2</sup>
</div>

<div>
  <sup>1</sup>School of Computer Science and Technology, East China Normal University
  <br>
  <sup>2</sup>Institute of Image Communication and Information Processing, Shanghai Jiao Tong University
  <br>
  <sup>3</sup>School of Humanities, Shanghai Jiao Tong University
  <br>
  <sup>*</sup>Both authors contributed equally to this research
  <sup>&dagger;</sup>Corresponding authors 
  <br>
  <br>
</div>   

<!-- 中文版速递：[知乎](https://zhuanlan.zhihu.com/p/10309270594) -->

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="figures/teaser.png">
  </div>
</div>
<br>

> Overview of the proposed **Oracle-P15K** dataset. The dataset comprises 14,542 OBI images with structure-aligned expert-annotated glyphs. Based on this, we present a pseudo OBI image generator, namely **OBIDiff**, to alleviate the long-tail distribution problem in current OBI datasets. Extensive experiments demonstrate both the necessity of Oracle-P15K and the effectiveness of OBIDiff in improving the performance of downstream OBI tasks.

## Release 🚀
- [2025/8/3] ⚡️ Dataset, code, pre-trained models are released !
- [2025/7/6] ⚡️ Our paper has been accepted by ACM MM 2025 !
- [2025/4/13] ⚡️ [Github repo](https://github.com/OBI-Future/Oracle-P15K) for **Oracle-P15K** is online !

## Code 💻

Create a conda environment and install dependencies.

Attach a control net to the SD model:

```
python tool_add_control.py ./models/v1-5-pruned.ckpt ./models/control_sd15_ini.ckpt
```

Organize the dataset into a JSON file：

```
python anno.py
```

Training & Testing. 

Dataset and checkpoint are available at [huggingface](https://huggingface.co/datasets/lomljhoax/Oracle-P15K) and [google drive](https://drive.google.com/file/d/18Hh0bzl-a5BfI1Z-56KmRF8ZOqIWwprB/view?usp=drive_link). We suggest to modify some logger settings when conducting evaluation. The notes are provided in [logger.py](obidiff/logger.py).

## Motivations 💡

The existing OBI datasets suffer from a long-tail distribution problem. Consequently, OBI-related models achieve superior performance in majority classes while underperforming in minority classes. Therefore, we construct **Oracle-P15K**, a large-scale structure-aligned OBI dataset comprising **14,542** images infused with domain knowledge from OBI experts. The Oracle-P15K dataset can also serve as a comprehensive benchmark for researchers to develop and evaluate their methods for dealing with other OBI information processing tasks, such as OBI denoising, recognition, etc.

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="figures/datasets.png">
  </div>

## Construction Pipeline 🧩

Focusing on **structure-aligned** image pairs for OBI generation and denoising models.

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="figures/pipeline.png">
  </div>

## Pseudo OBI Generator 🤖

Our **OBIDiff** consists of an autoencoder, a stable diffusion (SD) model, a glyph encoder, and a style encoder. Given a clean glyph image and a target rubbing-style image, it can effectively transfer the noise style of the original rubbing to the glyph image.

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:60%" src="figures/method.png">
  </div>

## Results on OBI Generation and Denoising Tasks 📌

<details close>
<summary>Qualitative results on the OBI generation tasks (click to expand)</summary>

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="figures/generation.png">
  </div>
</details>

<details close>
<summary>Quantitative results on the OBI generation tasks (click to expand)</summary>

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="figures/quant_gen.png">
  </div>

- Fitted kernel distribution of four low-level features including brightness, contrast, sharpness, and spatial information (SI):

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="figures/features.png">
  </div>

- Recognition accuracy of augmented images generated by the proposed OBIDiff and other OBI generation methods w.r.t. the scale of data augmentation:

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:60%" src="figures/scales.png">
  </div>
</details>

<details close>
<summary>Qualitative results on the OBI denoising tasks (click to expand)</summary>

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="figures/denoising.png">
  </div>
</details>

<details close>
<summary>Quantitative results on the OBI denoising tasks (click to expand)</summary>

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="figures/quant_den.png">
  </div>
</details>

## User Preference Study 👥

We develop a web-based [user interface](https://ljholyground.github.io/) with automated navigation to facilitate the evaluation process.

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:60%" src="figures/user.png">
  </div>
</details>

## Contact ✉️

Please contact the first author of this paper for queries.

- Jinhao Li, `lomljhoax@stu.ecnu.edu.cn`

## Citation 📎

If you find our work interesting, please feel free to cite our paper:
```
@misc{li2025mitigatinglongtaildistributionoracle,
      title={Mitigating Long-tail Distribution in Oracle Bone Inscriptions: Dataset, Model, and Benchmark}, 
      author={Jinhao Li and Zijian Chen and Runze Dong and Tingzhu Chen and Changbo Wang and Guangtao Zhai},
      year={2025},
      eprint={2504.09555},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2504.09555}, 
}
```

## <a name="acknowledgements"></a> Acknowledgements 🏆

This work was supported by the National Social Science Foundation of China (24Z300404220), Shanghai Jiao Tong University Key Project of Intelligent Humanities and Social
Sciences (ZHWK2506), and the National Social Science Foundation (Arts) Major Project (22ZD05).
