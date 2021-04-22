

def edgefunc_solid(meaningful_list,dict_of_ids):

#1)for solid edge with labels

#step)7.1

#making list of list of data
  directed_without_dash_edge_data = []


  
  for x in range(len(meaningful_list)):
    picked_item_str = meaningful_list[x]  #'StudentAgent(SA)_S3_E2'

    picked_item_str_list = picked_item_str.split("_")  #E.G ['StudentAgent(SA),'S3','E2']

    if len(picked_item_str_list) == 3:

      if picked_item_str_list[0][0:2] == 'St' and picked_item_str_list[2][0] =='E':
        
        directed_without_dash_edge_data.append(picked_item_str_list)



      if picked_item_str_list[0][0] == 'E' and picked_item_str_list[2][0:2] =='St':
         
        directed_without_dash_edge_data.append(picked_item_str_list)

      
      if picked_item_str_list[0][0:3] == 'Col' and picked_item_str_list[2][0] =='E':
        
        directed_without_dash_edge_data.append(picked_item_str_list)


      if picked_item_str_list[0][0] == 'E' and picked_item_str_list[2][0:3] =='Col':
        
        directed_without_dash_edge_data.append(picked_item_str_list)
    

   #output

   # directed_without_dash_edge_data= [['StudentAgent(SA)', 'S3', 'E2'],
    #['E3', 'S6', 'CollegeAgent(CA)'],
    # ['E4', 'S9', 'StudentAgent(SA)'], 
    # ['E4', 'S9', 'StudentAgent(SA)'],
    # ['CollegeAgent(CA)', 'S10', 'E5'], 
   #['E5', 'S11', 'StudentAgent(SA)'], 
  # ['E6', 'S13', 'StudentAgent(SA)']     ]


#step7.2)
#updating  id from dict values and 

  for x in range(len(directed_without_dash_edge_data)):

    for y in range(3):
      tempkey = directed_without_dash_edge_data[x][y]

      if tempkey in dict_of_ids:
        directed_without_dash_edge_data[x][y] = dict_of_ids.get(tempkey)
      else:
        pass
 


 # directed_without_dash_edge_data= [[14, 'S3', 2],
    #[3, 'S6', 15],
    # ['E4', 'S9', 'StudentAgent(SA)'], 
    # ['E4', 'S9', 'StudentAgent(SA)'],
    # ['CollegeAgent(CA)', 'S10', 'E5'], 
   #['E5', 'S11', 'StudentAgent(SA)'], 
  # ['E6', 'S13', 'StudentAgent(SA)']     ]
   

#step7.3)

#removing redundant atrributes
  templist = []
  for x in directed_without_dash_edge_data:
    if x not in templist:
      templist.append(x)

  directed_without_dash_edge_data = templist.copy()



#step7.4)
#coverting list of list to flat list
  directed_without_dash_edge_data_ids  = []

  for i in range(len(directed_without_dash_edge_data)):

    for j in range(3):
      directed_without_dash_edge_data_ids.append(directed_without_dash_edge_data[i][j]) 

  directed_without_dash_edge_len = len(directed_without_dash_edge_data_ids)

  #directed_without_dash_edge_data_ids =[14, 'S3', 2, 3, 'S6', 15, 4, 
 # 'S9', 14, 15, 'S10', 5, 5, 'S11', 14, 6, 'S13', 14]
 
  #output directed_without_dash_edge_len =18

  return directed_without_dash_edge_data_ids
   




def edgefunc_dotted(meaningful_list,dict_of_ids):
    directed_with_dash_edge_data = []

    for x in range(len(meaningful_list)):
        picked_item_str = meaningful_list[x]

        picked_item_str_list = picked_item_str.split("_")

        if len(picked_item_str_list) == 3:
            if picked_item_str_list[0][0:2] == 'St' and picked_item_str_list[2][0] =='C':
                directed_with_dash_edge_data.append(picked_item_str_list)

            if picked_item_str_list[0][0] == 'C' and picked_item_str_list[2][0:2] =='St':
                directed_with_dash_edge_data.append(picked_item_str_list)

            if picked_item_str_list[0][0:3] == 'Col' and picked_item_str_list[2][0] =='C':
                directed_with_dash_edge_data.append(picked_item_str_list)

            if picked_item_str_list[0][0] == 'C' and picked_item_str_list[2][0:3] =='Col':
                directed_with_dash_edge_data.append(picked_item_str_list)
    

   

#updating  id from dict values and 

    for x in range(len(directed_with_dash_edge_data)):

      for y in range(3):
        tempkey = directed_with_dash_edge_data[x][y]

        if tempkey in dict_of_ids:
          directed_with_dash_edge_data[x][y] = dict_of_ids.get(tempkey)
        else:
          pass
    


#removing redundant atrributes
    templist = []
    for x in directed_with_dash_edge_data:
      if x not in templist:
        templist.append(x)

    directed_without_dash_edge_data = templist.copy()




#coverting list of list to flat list
    directed_with_dash_edge_data_ids  = []

    for i in range(len(directed_with_dash_edge_data)):

      for j in range(3):
        directed_with_dash_edge_data_ids.append(directed_with_dash_edge_data[i][j])

 
    return directed_with_dash_edge_data_ids 











def edgefunc_solid_red(meaningful_list,dict_of_ids):
    nondirected_thickred_edge_data = []

    for x in range(len(meaningful_list)):
        picked_item_str = meaningful_list[x]

        picked_item_str_list = picked_item_str.split("_")

        if len(picked_item_str_list) == 2:
            if picked_item_str_list[0][0] == 'E' and picked_item_str_list[1][0] =='C':
                nondirected_thickred_edge_data.append(picked_item_str_list)

            if picked_item_str_list[0][0] == 'C' and picked_item_str_list[1][0] =='E':
                nondirected_thickred_edge_data.append(picked_item_str_list)

   

#updating  id from dict values and 

    for x in range(len(nondirected_thickred_edge_data)):

      for y in range(2):
        tempkey = nondirected_thickred_edge_data[x][y]

        if tempkey in dict_of_ids:
          nondirected_thickred_edge_data[x][y] = dict_of_ids.get(tempkey)
        else:
          pass
    


#removing redundant atrributes
    templist = []
    for x in nondirected_thickred_edge_data:
      if x not in templist:
        templist.append(x)

    nondirected_thickred_edge_data = templist.copy()




#coverting list of list to flat list
    nondirected_thickred_edge_data_ids  = []

    for i in range(len(nondirected_thickred_edge_data)):

      for j in range(2):
        nondirected_thickred_edge_data_ids.append(nondirected_thickred_edge_data[i][j])

 
    return nondirected_thickred_edge_data_ids 







