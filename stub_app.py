import time

import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

if "pocket_pilots" not in st.session_state:
    st.session_state.pocket_pilots = [
        { 
          "key": "wildfire_rescue_agent",
          "name": "🔥 Wildfire Rescue Agent",
          "prompt": "Provide real-time updates, evacuation guidance, safety procedures, and emergency support to help me prepare for and respond to an approaching wildfire." ,
          "messages": [
              {"role": "assistant", "content": "How can I help you?"}
          ]
        },
        { 
          "key": "antarctica_tour_guide",
          "name": "🧊 Antarctica Tour Guide",
          "prompt": "Information on local wildlife, historical sites, safety tips for extreme weather, and help with navigation and travel arrangements in Antarctica." ,
          "messages": [
              {"role": "assistant", "content": "How can I help you?"}
          ]
        }
    ]

if "create_pocket_pilot_name" not in st.session_state:
    st.session_state.create_pocket_pilot_name = ""

if "create_pocket_pilot_prompt" not in st.session_state:
    st.session_state.create_pocket_pilot_prompt = ""

def set_page(page_name):
    st.session_state.page = page_name

def add_pocket_pilot(name, prompt):
    st.session_state.create_pocket_pilot_name = name
    st.session_state.create_pocket_pilot_prompt = prompt

    key = name.lower().replace(" ", "_")
    
    st.session_state.pocket_pilots.append({
        "key": key,
        "name": name,
        "prompt": prompt,
        "messages": [
            {"role": "assistant", "content": "How can I help you?"}
        ]
    })
    
    set_page(key)

with st.sidebar:
    st.header("Create a new Pocket Pilot")
    
    create_name = st.text_input(
        "Name",
        key="create_name",
        type="default",
    )

    create_prompt = st.text_input(
        "Prompt",
        key="create_prompt",
        type="default",
    )

    if st.button("Generate"):
        with st.status("Building Pocket Pilot...") as status:
            st.write("Fetching data...")
            time.sleep(1)
            st.write("Downloading model.")
            time.sleep(1)
            st.write("Training model...")
            time.sleep(1)
            status.update(label="Done!", state="complete", expanded=False)
        add_pocket_pilot(create_name, create_prompt)

    st.divider()

    if st.button("Home", use_container_width=True):
        set_page("home")

    st.header("Pocket Pilots")

    for pilot in st.session_state.pocket_pilots:
      if st.button(pilot["name"], use_container_width=True):
          set_page(pilot["key"])

if st.session_state.page == "home":
    st.title("Welcome to Pocket Pilot 🧑‍✈️")
    st.caption("A platform for building specialty assistants for offline use")

    st.write("To get started, you can either,")
    st.write("1) Start chatting with one of your pocket pilots")
    st.write("2) Create a new pocket pilot with a prompt and download it to your device")
else:
    for pilot in st.session_state.pocket_pilots:
        if st.session_state.page == pilot["key"]:
            st.title(pilot["name"])
            st.caption("Prompt: " + pilot["prompt"])
    
            for msg in pilot["messages"]:
                st.chat_message(msg["role"]).write(msg["content"])
            
            if prompt := st.chat_input():
              pilot["messages"].append({"role": "user", "content": prompt})
              st.chat_message("user").write(prompt)
              with st.spinner("Thinking 🤔..."):
                time.sleep(3)
                msg = {"role": "assistant", "content": "(Assistant response)"}
                pilot["messages"].append(msg)
                st.chat_message("assistant").write(msg["content"])
