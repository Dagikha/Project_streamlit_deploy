import streamlit as st

# st.set_page_config(layout="wide")
# st.markdown("""
#     <style>
#     [data-testid=stSidebarNav] {
#         display:none;
#         }
#     </style>
# """, unsafe_allow_html=True)


#Wrap menu:


#dữ liệu của các món ăn(st.session_state)
if "lst_mon_an" not in st.session_state:
    st.session_state.lst_mon_an =[]

st.title("Menu KFC mini")

dict_menu = {
    "ga_ran":50000,
    "bo":55000,
    "pepsi":15000,
    "kem":20000,
    "khoai_tay":25000
}


col1,col2 = st.columns(2)

with col1:
    st.header("Chọn Món ăn")
    frm_mon_an =  st.form("frm_mon_an")
    with frm_mon_an:
        # st.title("chọn món ăn")
        dict_menu["ga_ran"] = st.number_input("Gà rán",min_value=0,step=1) * dict_menu["ga_ran"]
        dict_menu["bo"] = st.number_input("Bò",min_value=0,step=1) * dict_menu["bo"]
        dict_menu["khoai_tay"] = st.number_input("Khoai tây chiên",min_value=0,step=1) * dict_menu["khoai_tay"]
        dict_menu["pepsi"] = st.number_input("Pepsi",min_value=0,step=1) * dict_menu["pepsi"]
        dict_menu["kem"] = st.number_input("Kem",min_value=0,step = 1) * dict_menu["kem"]
        
        btn = frm_mon_an.form_submit_button(label="Đặt món")
    
    
        
with col2:
    st.header("Hoá đơn của bạn")
    st.table(dict_menu)
    lst_mon_an = []
    Sum = 0
    for i in dict_menu:
        Sum += dict_menu[i]
    Sum = f"{Sum:,}"
    st.subheader(f"Tổng tiền: {Sum} VND")
    
    # for i in dict_menu:
    #     lst_mon_an.append(dict_menu[i])


