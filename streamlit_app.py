import streamlit as st
import requests 

##Variables
packet_array = [];
def main():
    st.title("Welcome to MTS Mobile Micro Manager!")
    url = st.text_input('Enter the URL to scrape data from', "https://asp-interface.arc.nasa.gov/API/parameter_data/N806NA/PICARD")
    full_packet = requests.get(url);
    data_string = full_packet.text;
    packet_list = data_string.split(",");
    packet_array.append(packet_list);
    st.text(packet_list)

if __name__ == "__main__":
    main()