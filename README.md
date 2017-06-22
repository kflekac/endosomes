# Endosomes
This repository contains the supplementary files, certain code files, some of the data and high-resolution images that were involved in the study of my MSc Bioinformatics project on network analysis and investigations of the endosomal system.


## Supplementary Files

### **Supplementary 1**
A list of Gene Ontology 'cellular compartment’ annotations that are associated with the endosome. Annotations originally accessed February 2016

### **Supplementary 2**
The complete *H.Sapiens* protein-protein interaction list. This data was derived from semi-manually combined [PINA v2.0 database](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3244997/) (accessed January 2016, last updated 2014), and the [InnateDB database’s](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3531080/) Experimentally Verified Interactions (Accessed 25 June 2016, updated weekly).

This data is currently in [PSI-MITAB 2.5](http://www.psidev.info/node/60 "HUPO PSI-MI 2.5 XML Documentation") format, with the exception of:
+ An additional undirected ‘interactions’ column, found in column 4. This contains the lexically sorted interaction IDs of the Interactor A and Interactor B proteins, with an "(interacts with)" string between each.
+ 3 additional columns at the end of the file, containing the number of unique pubmed identifiers for that interaction (**NumPubs**), the number of unique methods used to confirm that interaction (**NumMethods**), and the calculated weight score for that interaction (**Weight**), as defined by the novel weighting interaction detailed in my report.
+ This data has had HGNC approved gene symbols added for each interactor

### **Supplementary 3**
The 1st order expansion of the endosomal network, as extracted from the combined PPI dataset in Supplementary 2. Uses proteins specified in Supplementary 6 as the 0th order network.

### **Supplementary 4**
The results of the BiNGO over-representation analysis, as performed on the network of endosomal proteins found to be commonly expressed across all three of the macrophage, epithelial and neuroblastoma cell-line data. This test was performed on the GO biological process annotations found within the network, in comparison to the entire biological process ontology.

### Supplementary 5
The 1706 gene product entries (as extracted from GO) annotated with any of the GO cellular compartment annotations found within Supplementary 1

### Supplementary 6
A list of the final, curated early endosome set of gene products. 
Contains the Uniprot Accession, Gene Symbol, Gene/Protein Name, and whether these entries were chosen due to manual curation (expert curation by Prof. P. Gleeson) or network curation (as detailed in the report, methods section 2.1.2.1).

### Supplementary 7
The total protein-protein interaction file, as found in Supplementary 3, after the applciation of a >= 0.5 filter to the *weight* column
Contains 5200 entries, between 2090 different interactors.

### Supplementary 8
Image of the "Core Network", where nodes found to be contained within all three of the threshold-filtered macrophage, monocyte and dendritic cell networks were extracted.

### Supplementary 9
All 4200 of the significantly differentially expressed genes founds between the monocyte and dendritic cell populations ([derived from the Klug et al 2010 study](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL6848 "GEO Entry for GSE19236, from array GPL6848"))

### Supplementary 10
All 3900 of the significantly differentially expressed genes founds between the monocyte and macrophage cell populations ([derived from the Klug et al 2010 study](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL6848 "GEO Entry for GSE19236, from array GPL6848"))

### Supplementary 11
Image of the "Core Network", where nodes found to be contained within all three of the macrophage, monocyte and dendritic cell networks were extracted.

### Supplementary 12
Network image of the 400 genes (and 1000 interactions) lost from the core network in supplementary 11

### Supplementary 13
A network representation of the results of the BiNGO analysis explained in supplementary 4. Nodesw are coloured from orange to white according to p-value (0 to 1), and the size is directly correlated to the number of nodes attributed with that annotation. 
Image contains labelled boxes around sections of the entwork with a high amount of annotations relating to:
A. T-Cell Regulation
B. Apoptosis regulation
C. Cellular defence/immune response
D. Protein localisation and transport
E. Regulation of various signalling pathways
F. Cell adhesion, motility and migration

### Supplementary 14
The KEGG binary pathway association file. All pathways and protein associations are current as of January 2017.

### Supplementary 15
The KEGG binary file, as found in supplementary 14, containing only those proteins found in the unweighted endosomal network.
This file has also had an additional 2 rows added, containing the number of endosomal proteins present within a particular pathway, and the percentage involvement of of the endosome in that pathway as compared to the total number of proteins involved.

### Supplementary 16
A DAVID over-representation analysis, for all KEGG pathways and the proteins contained within the unweighted endosomal network.
