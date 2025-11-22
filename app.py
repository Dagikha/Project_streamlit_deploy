import streamlit as st

st.set_page_config(layout="wide")
st.markdown("""
    <style>
    [data-testid=stSidebarNav] {
        display:none;
        }
    </style>
""", unsafe_allow_html=True)
# st.markdown(css,unsafe_allow_html=True)

st.title("Admin Dashboard")
col1,col2,col3,col4 = st.columns(4)


with col1:
    st.header("Tổng doanh thu")
    st.metric("Doanh thu","12.5 M","+10%")
    
with col2:
    st.header("Người dùng mới")
    st.metric("New account","18","+10%")
    
with col3:
    st.header("Đơn hàng")
    st.metric("Packages","327",delta="+11.5%")
    
with col4:
    st.header("Tiền chuyển đổi")
    st.metric("Currency",value="142",delta="-5%")
    
st.markdown("<hr/>",True)

col_char_1,col_char_2 = st.columns(2)

with col_char_1:
    st.header("Doanh thu 7 ngày gần nhất")
    st.line_chart([100,90,245,250,430,350,290])
    
with col_char_2:
    st.header("Số lượng đơn theo trạng thái")
    st.bar_chart([28,90,22,56])
    


#sidebar
st.sidebar.title("Admin")
st.sidebar.subheader("Trang 2")
st.sidebar.markdown("<hr/>",True)
st.sidebar.title("Menu")
st.sidebar.page_link("pages/bao_cao.py",label="Report")
st.sidebar.page_link("pages/nguoi_dung.py",label="User")
st.sidebar.page_link("pages/bt_menu.py", label="Menu food")





