# simpleFunctions.py

class Not_number(Exception): pass

def sumList(m_list):
    for i in range(len(m_list)):
        t_int = str(m_list[i])
        if not t_int.isdigit():
           error_message = "value at index " + str(i) + " is not a number"
           raise Not_number, error_message
     
    return sum(m_list)
