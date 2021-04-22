  
from django.shortcuts import render
import json
import pandas as pd
from .edgefunc import edgefunc_dotted,edgefunc_solid_red,edgefunc_solid



def index(request):
    return render(request,'base.html')




def student_graph(request):
#step1) Input taken from user excel

  df_input = pd.read_csv("static/input.csv") 
  input_numbers_df = df_input.to_records(index=False)

  constraint_student = pd.read_csv("static/constraint_student.csv") 
  constraint_student_df = pd.DataFrame(constraint_student)



  number_of_events = input_numbers_df['no_of_events'][0]
  number_of_constraints = input_numbers_df['no_of_constraints'][0]
  number_of_services = input_numbers_df['no_of_services'][0]



#step2) sending agent names as it is to js   
  agent_names = constraint_student_df['Agent'].values.tolist();

  
  updated_agent_names = []
  
  #distinct agent names are captured in updated_agent_names
  
  for x in agent_names:
    if x not in updated_agent_names:
      updated_agent_names.append(x)
    else:
      pass

  agent_names = updated_agent_names.copy()

 #step3)json dumping for webpage sending 
 
  number_of_agents = len(agent_names)
  agent_names_cap = agent_names
  agent_names = json.dumps(agent_names)

#step4)creating dictionary of ids
  
  dict_of_ids = dict()
  
  incr = 1



  for x in range(int(number_of_events)):
    temp_e = 'E{}'.format(x + 1)
    dict_of_ids.update({temp_e:incr})
    incr+=1


  for x in range(int(number_of_constraints)):
    temp_c = 'C{}'.format(x + 1)

    dict_of_ids.update({temp_c:incr})
    incr+=1
 
  for x in range(int(number_of_agents)):
    dict_of_ids.update({agent_names_cap[x]:incr})
    incr+=1
  
#OUTPUT

 # dict_of_ids =  {'E1': 1, 'E2': 2, 'E3': 3, 'E4': 4, 'E5': 5, 'E6': 6, 'C1': 7, 'C2': 8,
  # 'C3': 9, 'C4': 10, 'C5': 11, 'C6': 12, 'C7': 13, 'StudentAgent(SA)': 14, 'CollegeAgent(CA)': 15}



#step5)dataframe to list
  df01 = constraint_student_df.to_html(classes=["table-bordered",])

  dataframe_copy_list = constraint_student_df.values.tolist();

#output
 # dataframe_copy_list = 

 #[['StudentAgent(SA)', 'S1:C1', 'E1', 'C2:S2'], 
# ['StudentAgent(SA)', 'S3', 'E2', 'C3:S4'],
# [StudentAgent(SA)', 'S5:C4', 'E3', 'S6'], 
 # ['CollegeAgent(CA)', 'S7:C5', 'E4', 'S9'],
 # ['CollegeAgent(CA)', 'S8:C7', 'E4', 'S9'],
  # ['CollegeAgent(CA)', 'S10', 'E5', 'S11'],
 #  ['CollegeAgent(CA)', 'S12:C6', 'E6', 'S13']  ]


#step6)dataframe_copy_list to meaningful list
  
  meaningful_list = []
  
  first_pos_S = False
  first_pos_C = False
  
  for x in range(len(dataframe_copy_list)):
    for y in range(len(dataframe_copy_list[x])):
      if y == 0:
        continue
      else:                              # 0  2
        entry_picked = dataframe_copy_list[x][y] #e.g  'S1:C1'(one of the entry)

#case1      
        if len(entry_picked) == 5 or len(entry_picked) == 6:   #if len of entry is 5 or 6
          entry_picked_list = entry_picked.split(":") #entry_picked_list = ['S1','C1']

          if entry_picked_list[0][0] == 'S':  #if len of entry starts with S
            first_pos_S =True
            temp_str = str(dataframe_copy_list[x][0]) + '_' + entry_picked_list[0] + '_' + entry_picked_list[1]
            meaningful_list.append(temp_str)


          else:            #if len of entry starts with C
            first_pos_C = True
            if dataframe_copy_list[x][0] == "StudentAgent(SA)":
              post_attach = 'CollegeAgent(CA)'
            else:
              post_attach = 'StudentAgent(SA)'

 
            temp_str = entry_picked_list[0] + '_' + entry_picked_list[1] + '_' +post_attach
            meaningful_list.append(temp_str) 
          
#case2  
        if entry_picked[0] == 'E':    #e.g 'E1'(one of the entry)
          item1 = dataframe_copy_list[x][y-1] #e.g 'S1:C1'  // 'S3'

          if len(item1) >= 5:
            templist = item1.split(":")   # ['S1','C1']
            attachment = templist[1] + '_' + dataframe_copy_list[x][y]
            meaningful_list.append(attachment)


          else:
            templist = item1.split(":") #e.G ['S3']
            attachment = dataframe_copy_list[x][0] + "_" + templist[0] + "_" + dataframe_copy_list[x][y]
            meaningful_list.append(attachment)

############################################################## below this repair
          item2 = dataframe_copy_list[x][y+1]   #e.g 'C2:S2'

          if len(item2) >= 5:
            templist = item2.split(":")  #['C2','S2']
            attachment =  dataframe_copy_list[x][y] + '_' + templist[0]
            meaningful_list.append(attachment)

          else:
            templist = item2.split(":") #E.G 'S6'
            if dataframe_copy_list[x][0] == "StudentAgent(SA)":
              post_attach = 'CollegeAgent(CA)'
            else:
              post_attach = 'StudentAgent(SA)'


            attachment =  dataframe_copy_list[x][y]  +"_" + templist[0]  + "_"+ post_attach
            meaningful_list.append(attachment)

#output 
#meaningful_list = 
#['StudentAgent(SA)_S1_C1', 'C1_E1', 'E1_C2', 'C2_S2_CollegeAgent(CA)',
# 'StudentAgent(SA)_S3_E2', 'E2_C3', 'C3_S4_CollegeAgent(CA)', 
#'StudentAgent(SA)_S5_C4', 'C4_E3', 'E3_S6_CollegeAgent(CA)', 
#'CollegeAgent(CA)_S7_C5', 'C5_E4', 'E4_S9_StudentAgent(SA)', 
#'CollegeAgent(CA)_S8_C7', 'C7_E4', 'E4_S9_StudentAgent(SA)', 
#'CollegeAgent(CA)_S10_E5', 'E5_S11_StudentAgent(SA)', 'CollegeAgent(CA)_S12_C6', 
#'C6_E6', 'E6_S13_StudentAgent(SA)']





#step7)edges drawing analysis



#step7 repeat 1st time) for dashed edge without dotted 
    
  directed_without_dash_edge_data_ids = edgefunc_solid(meaningful_list,dict_of_ids)

  directed_without_dash_edge_len = len(directed_without_dash_edge_data_ids)

   

#step7 repeat 2nd time) for dashed edge with labels
    
  directed_with_dash_edge_data_ids = edgefunc_dotted(meaningful_list,dict_of_ids)

  directed_with_dash_edge_len = len(directed_with_dash_edge_data_ids)

   

#step7 repeat 3rd time) for thick red edges

  nondirected_thickred_edge_data_ids = edgefunc_solid_red(meaningful_list,dict_of_ids)

  nondirected_thickred_edge_data_ids_len = len(nondirected_thickred_edge_data_ids)


#step7 ends




  context = {'number_of_events':number_of_events,
              'number_of_constraints':number_of_constraints,
              'number_of_agents':number_of_agents,
              'agent_names':agent_names,
              'dict_of_ids' : dict_of_ids,
              'dataframe_copy_list':dataframe_copy_list,
              'df01':df01,
              'agent_names':agent_names,
              'meaningful_list':meaningful_list,
              'directed_without_dash_edge_len':directed_without_dash_edge_len,
              'directed_without_dash_edge_data_ids':directed_without_dash_edge_data_ids,
              'directed_with_dash_edge_len':directed_with_dash_edge_len,
              'directed_with_dash_edge_data_ids':directed_with_dash_edge_data_ids,
              'nondirected_thickred_edge_data_ids_len':nondirected_thickred_edge_data_ids_len,
              'nondirected_thickred_edge_data_ids':nondirected_thickred_edge_data_ids,


              }



  return render(request,'figure4.html',context)


