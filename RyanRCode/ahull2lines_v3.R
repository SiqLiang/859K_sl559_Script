ahull2lines <- function(hull){
  arclist <- hull$arcs
  arclist <- arclist[arclist[,"theta"] != 0, ]
  arclist <- cbind(arclist, Rev = 0)
  lines <- list()
  
  temp.arclist <- head(arclist, 1)
  arclist <- arclist[-1,]
  while(nrow(arclist)>1){
    last <- tail(temp.arclist, 1)[,"end2"]
    if(last %in% arclist[,"end1"]){
      ind <- which(arclist[,"end1"] == last)
      temp.arclist <- rbind(temp.arclist, arclist[ind,])
      arclist <- arclist[-ind,]
    }else if(last %in% arclist[,"end2"]){
      ind <- which(arclist[,"end2"] == last)
      end1<-arclist[ind,"end1"]
      end2<-arclist[ind,"end2"]
      arclist[ind,"end1"] <- end2
      arclist[ind,"end2"] <- end1
      arclist[ind,"Rev"] = 1
      temp.arclist <- rbind(temp.arclist, arclist[ind,])
      arclist <- arclist[-ind,]
    }else {
      temp.arclist <- rbind(temp.arclist, arclist[1,])
      arclist <- arclist[-1,]
    }
    if(is.null(nrow(arclist))){ #OPERATION BREAKS ON LAST ROW
      last <- tail(temp.arclist, 1)[,"end2"]
      if(last %in% arclist["end1"]){
        temp.arclist <- rbind(temp.arclist, arclist)
      }else {
        end1<-arclist["end1"]
        end2<-arclist["end2"]
        arclist["end1"] <- end2
        arclist["end2"] <- end1
        arclist["Rev"] = 1
        temp.arclist <- rbind(temp.arclist, arclist)
      }
      break
    }
  }
  arclist <- temp.arclist
  
  for (i in 1:nrow(arclist)) {
    # Extract the attributes of arc i
    center_i <- arclist[i, 1:2]
    radius_i <- arclist[i, 3]
    vector_i <- arclist[i, 4:5]
    theta_i <- arclist[i, 6]
    # Convert arc i into a Line object
    line_i <- arc2line(center = center_i, r = radius_i, vector = vector_i, theta = theta_i)
    if(arclist[i,9]==1){
      line_i@coords<-line_i@coords[nrow(line_i@coords):1,]
    }
    list_length <- length(lines)
    if(list_length > 0){
      # If a line has already been added to the list of lines
      # Define last_line_coords as the coordinates of the last line added to the list before the ith line
      last_line_coords <- lines[[list_length]]@coords
    }
    if(i == 1){
      # Add the first line to the list of lines
      lines[[i]] <- line_i
    } else if(isTRUE(all.equal(line_i@coords[1,], last_line_coords[nrow(last_line_coords),]))){
      # If the first coordinate in the ith line is equal to the last coordinate in the previous line
      # then those lines should be connected
      # Row bind the coordinates for the ith line to the coordinates of the previous line in the list
      #print(paste0(i," Same Line"))
      lines[[list_length]]@coords <- rbind(last_line_coords, line_i@coords[2:nrow(line_i@coords),])
    } else {
      #print(paste0(i," Not Same Line"))
      # If the first coordinate in the ith line does not match the last coordinate in the previous line
      # then the ith line represents a new line
      # Add the ith line to the list as a new element
      lines[[length(lines) + 1]] <- line_i
    }
  }
  # Convert the list of lines to a Line object
  lines <- Lines(lines, ID = 'l')
  # Convert the Line object to a SpatialLines object
  sp_lines <- SpatialLines(list(lines))
  return(sp_lines)
}