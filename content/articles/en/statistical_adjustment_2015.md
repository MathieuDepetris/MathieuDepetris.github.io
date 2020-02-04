title: Statistical adjustment of a sample
image: /pictures/portfolio/redressement_statistique_2015.jpg
summary: Development of a statistical adjustment function.
Author: Depetris M.
date: 2019-02-02
lang: en

## Statistical adjustment of a sample

<font color="#238896"><strong>Structure:</strong></font> Ifremer station of Brest
<br><font color="#238896"><strong>Date:</strong></font> 2015

### Principles and objectives

<p style="text-align: justify">
The objective of sample adjustment (or margin calibration) is to improve the representativeness of the sample on a number of qualifying criteria also known as auxiliary variables. The underlying principle is that only a sample with the same structure as the parent population on the criteria known from this population allows the answers obtained on the other criteria to be generalised to the whole of this population. The adjustment therefore seeks to apply weights to individuals in order to increase the weight of those belonging to under-represented groups in the sample surveyed in relation to the parent population, and at the same time to reduce the weight of those who are over-represented.
</p>

<p style="text-align: justify">
Specifically, the aim is to obtain comparable distributions between the population and the sample. We will therefore associate an adjustment weight to each data item (by default the weight of each data item is identical and equal to the sampling rate: n sample / N population).
</p>

### Programming the function

<p style="text-align: justify">
During my time at the Ifremer Fisheries Biology Laboratory in Brest, I worked with Sébastien Demanèche (LBH Ifremer Brest) to develop a function under R to calculate the adjustment weights of a sample. It uses the "survey" package developed by Professor Thomas Lumley, and more precisely the "calibrate" function.
</p>

### Prospects and future developments

<p style="text-align: justify">
The first tests were conclusive and showed a clear improvement in the calculations derived from the rectified sample compared to the unrectified sample. However, the main objective of the function (its generalization to any "type" of sample) raises many questions. For example, it will be necessary to group certain modalities within the variables to avoid non-convergence of the function (in cases where there are very few occurrences for certain modalities). In addition, the selection of auxiliary variables will need to be further investigated. The limits of the adjustment, including the precision variable, depend very much on the auxiliary variables used.
</p>
