
import statistics
import json
import collections
from datetime import datetime

from utils import connect_db



def calculate_stats():
    st, names = connect_db()
    if st is None or names is None:
        raise Exception("Database connection failed or no data found.")
      
    st = filter_categories(st, names)
    convert_yn_to_nums(st)
    hos_dic = sort_by_hospital(st)
    return calculate_results(hos_dic)

class Story:
    date='1999'
    story =''
    tags=''

    def __str__(self):
        return json.dumps(self)

def filter_categories(data,names):
    ngg = tuple()
    for n in names:
        ngg= (*ngg, n[0])
    diction = dict()
    i=0
    
    for x in data:
        st = Story()
        while(i<len(x)):
            if i==1:
                st.date =x[i]
            if i==46: 
                if x[i]==None:
                    st.tags='None'
                else:
                    st.tags=x[i]
            if i==47:
                if x[i]=='':
                    st.story='None'
                    
                else:
                    st.story=x[i]
            diction.setdefault(x[0],[]).append((ngg[i],x[i]))
            i+=1
        diction.setdefault(x[0],[]).append(('storyObj',st.__dict__))
        i=0
    
    

    for y in diction:
        to_del = diction[y]
        if to_del[51] == 0:
            remove_story = list(to_del[47])
            remove_story[1]=''
            to_del[47] = tuple(remove_story)
        del to_del[48:52]
        # del to_del[48:]
        del to_del[28:45]
        if to_del[24][1] == 'לא':
            z = list(to_del[25])
            z[1]=0.0
            to_del[25] = tuple(z)
        del to_del[24:25]
        del to_del[3:11]
        del to_del[0]
    return diction


def sort_by_hospital(data):
    by_dict = dict()
    """ insert in dictionary"""
    for x in data:
        by_dict.setdefault(data[x][1][1], []).append(data[x][2:])
    return by_dict


def convert_yn_to_nums(data):
    for x in data:
        
        for y in range(len(data[x])):
            convert_list = list(data[x][y])
            if y == 11:
                if convert_list[1] == 'כן':
                    convert_list[1] = '1'
                elif convert_list[1] == 'לא':
                    convert_list[1] = '5'
            else:
                if convert_list[1] == 'כן':
                    convert_list[1] = '5'
                elif convert_list[1] == 'לא' or convert_list[1] == 'לא יודעת':
                    convert_list[1] = '1'
            data[x][y] = tuple(convert_list)


def calculate_results(data):
    # 0 1 כבוד
    # פרטיות 5 1-5
    # 6-7 חסיון רפואי 2
    # בחירה מדעת 5 8-12
    # תמיכה רציפה 13
    # תקשורת אפקטיבית 1 14
    # שביעות רצון 1 15
    formula_inner = [1.0, 0.4, 0.15, 0.15, 0.15, 0.15, 0.5, 0.5, 0.25, 0.25, 0.25, 0.125, 0.125, 0.0, 1, 1, 1]
    formula_with_protest = [1.0, 0.4, 0.15, 0.15, 0.15, 0.15, 0.5, 0.5, 0.2, 0.2, 0.2, 0.1, 0.1, 0.2, 1, 1, 1]
    data_set = []
    dict_entries = dict()
    res_dict = dict()
    l=0
    
    for k in data:
        dict_entries[k] = len(data[k])
        num_of_entries = 0  # number of entries for a hospital
        for i in data[k]: # iterate over dictionary
            for x in range(len(i)): # -1 to ignore tags iteration
                for y in range(len(data[k])):
                    if data[k][y][x][1] != '':
                        if x == 1:
                            if data[k][y][x+1][1] == '':  # Privacy conditionals
                                data_set.append(float(data[k][y][x][1]))
                            else:
                                data_set.append(float(data[k][y][x][1]) * formula_inner[x])
                        elif 8 <= x <= 13:
                            if data[k][y][13][1] != 0.0:
                                data_set.append(float(data[k][y][x][1]) * formula_with_protest[x])
                            else:
                                # if x < 13:  ###
                                data_set.append(float(data[k][y][x][1]) * formula_inner[x])
                        elif 17<= x <= 19:
                            # stories + tags
                            data_set.append(data[k][y][x][1])
                        else:
                            data_set.append(float(data[k][y][x][1])*formula_inner[x])
                    else:
                        if x <17:
                            data_set.append(0.0)
                if x == num_of_entries:
                    if x >= 17:
                        st = data_set
                    elif len(data_set) > 0:
                        st = statistics.mean(data_set)
                    else:
                        st = 0.0
                    res_dict.setdefault(k, []).append(st)
                data_set = []
                num_of_entries += 1
    
    
    final_inner_dict = dict()
    final_outer_dict = dict()
    stories = dict()
    for ky in res_dict:
        final_inner_dict.setdefault(ky, []).append(res_dict[ky][0])  # Respect
        final_inner_dict.setdefault(ky, []).append(sum(res_dict[ky][1:6]))  # privacy
        final_inner_dict.setdefault(ky, []).append(sum(res_dict[ky][6:8]))   # Confidentiality
        final_inner_dict.setdefault(ky, []).append(sum(res_dict[ky][8:14]))  # Deciding
        final_inner_dict.setdefault(ky, []).append(res_dict[ky][14])  # Support
        final_inner_dict.setdefault(ky, []).append(res_dict[ky][15])  # Communication
        final_inner_dict.setdefault(ky, []).append(res_dict[ky][16])  # Satisfaction
        stories.setdefault(ky, []).append(res_dict[ky][19])  # Stories
    formula_outer = [0.15, 0.15, 0.1, 0.15, 0.1, 0.1, 0.25]
    for kx in final_inner_dict:
        final_outer_dict[kx] = 0
        for l in range(len(formula_outer)):
            final_outer_dict[kx] += final_inner_dict[kx][l] * formula_outer[l]
    dada = sorted(final_outer_dict.items(), key=lambda x: x[1], reverse=True)
    shcopy = collections.OrderedDict(dada)
   
    return final_inner_dict, shcopy, dict_entries, stories



def sort_stories_by_date(stories):
    # Convert date strings to datetime objects and sort in reverse order (newest to oldest)
    for key in stories:
        stories[key][0] = sorted(stories[key][0], key=lambda story: datetime.strptime(story['date'], '%d/%m/%Y'), reverse=True)
    return stories



