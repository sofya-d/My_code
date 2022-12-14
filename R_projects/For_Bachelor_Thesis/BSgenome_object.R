## creating mm39 bs genome
forgeBSgenomeDataPkg("./BSGenome.mm39/BSgenome.Mmusculus.UCSC.mm39-seed.txt")

## run in RStudio terminal
# "C:\Program Files\R\R-4.1.0\bin\R.exe" CMD build --no-build-vignettes --no-manual C:\Users\User\Documents\BSgenome.Mmusculus.UCSC.mm39
# "C:\Program Files\R\R-4.1.0\bin\R.exe" CMD check --no-manual --no-vignettes --no-build-vignettes C:\Users\User\Documents\BSgenome.Mmusculus.UCSC.mm39_1.60.0.tar.gz
# "C:\Program Files\R\R-4.1.0\bin\R.exe" CMD INSTALL C:\Users\User\Documents\BSgenome.Mmusculus.UCSC.mm39_1.60.0.tar.gz
