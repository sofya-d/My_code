music <- music[, 2:9]

music <- as.data.frame(music)

rownames(music) <- c("danceability", "energy", "speechiness", "valence", "acousticness")

library(heatmaply)

heatmaply(as.matrix(music), column_text_angle = 0, draw_cellnote = TRUE, cellnote_color = "white", cellnote_textposition = "middle center", Rowv = FALSE, Colv = TRUE, dendrogram = "column", show_dendrogram = c(F, T), xlab = "Music genre", ylab = "Ìusic characteristic", main = "Music characteristic severity in music genres", key.title = "score", labCol = c("Pop", "Rock", "Hip Hop", "Blues", "R&B", "Country", "Folk", "Jazz"))
