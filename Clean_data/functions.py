import pandas as pd
df = pd.read_csv("nom_du_csv.csv")

columns_names = {}
for x in df.columns.tolist():
    columns_names[df.columns.tolist().index(x)] = x
# For now, each row can be clean, without listing them by ourself
# In the future, we can make a dictionnary with only the sensible columns
# so as not to have a too long list of choices
    
def menu(choice_list):
    '''
    Fonction to make the choices of the columns to clean.
    If no argument is passed : there will be a menu to choose one or more columns.
    Elif the argument is the string "a" : all the columns will be selected.
    Or else, the argument can be a list of integers, each integers will clean the column it is associated with.
    Return a list of integers.
    '''
    
    y = -1
    clean_choice = []
    
    if choice_list == None:   
        while y != "q":
            print(columns_names)
            y = input("Wich columns do you want to clean? ( q => exit  // a => all)")
            try:
                y = int(y)
            except:
                if y == "a":
                    clean_choice = list(columns_names.keys())
                    break
                elif y == "q":
                    break
                print("Please, enter the column's number yo want to add : \n")
        
            if y != "q":
                clean_choice.append(y)

    elif choice_list == "a":
        clean_choice = list(columns_names.keys())

    else:
        for elem in choice_list:
            clean_choice.append(elem)
       
    return clean_choice




# For now, basic cleaning is in the whole clean, can be changed so the basic cleaning is only done once,
# and then the dataframe returned is saved, and we work from this one to choose wich columns to clean,
# without doing the basic cleaning agai each time

def clean(df, choice_list=None):
    '''
    Fonction to do all the steps of the cleaning in a dataset :
        1) All the basic cleaning (suppressing unnecessary columns, change type to int...)
        2) Choosing the columns that will be used
        3) Cleaning these columns
    arguments : dataframe (resquired), choice_list (if not, it'll be asked, this is a list of the columns that must be cleaned)
    return a cleaned dataframe with only the columns asked
    '''
    
    df = basic_clean(df)
    clean_choice = menu(choice_list)
    
    for i in clean_choice:
        
        print(columns_names[x] + " : " + str(df.shape[0]) + "rows before cleaning.")

        if i == 0: pass
        elif i == 1: pass
        elif i == 2: pass
        elif i == 3: pass
        elif i == 4: pass
        elif i == 5: pass
        elif i == 6: pass
        elif i == 7: pass
        elif i == 8: pass
        elif i == 9: pass
        elif i == 10: pass
        elif i == 11: pass
        elif i == 12: pass
        elif i == 13: pass
        elif i == 11: pass
        elif i == 12: pass
        elif i == 13: pass
        elif i == 14: pass
        elif i == 15: pass
        elif i == 16: pass
        elif i == 17: pass
        elif i == 18: pass
        elif i == 19: pass
            
        else:
            continue

        print(df.shape[0] + " rows after cleaning.")
         
    return df


def basic_clean(df):
    """
    Cleaning that don't remove row except for duplicates, but may remove unnecessary columns.
    Take a row dataframe, return a cleaner dataframe.
    """ 

    
    return df
