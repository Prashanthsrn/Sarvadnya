import streamlit as st
import networkx as nx
import streamlit.components.v1 as components
import json
import tempfile
from graph_builder import GraphBuilder


def main_ui():
    st.title("Graph Application")

    # Initialize session state
    if 'graph_obj' not in st.session_state:
        st.session_state.graph_obj = GraphBuilder()
    if 'selected_element' not in st.session_state:
        st.session_state.selected_element = None
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None

    # Create a two-column layout
    left_column, right_column = st.columns([1, 3])

    # Left column: Information Panel
    with left_column:
        st.header("Information Panel")
        if st.session_state.selected_element:
            element_type, element_id = st.session_state.selected_element
            if element_type == 'node':
                properties = st.session_state.graph_obj.get_node_properties(element_id)
                st.subheader(f"Node: {element_id}")
            else:
                source, target = element_id
                properties = st.session_state.graph_obj.get_edge_properties(source, target)
                st.subheader(f"Edge: {source} -> {target}")

            for key, value in properties.items():
                st.text(f"{key}: {value}")
        else:
            st.write("Click on a node or edge to view its properties.")

    # Right column: Graph Visualization and Import
    with right_column:
        # Import functionality
        st.header("Import Graph Data")

        if st.session_state.uploaded_file is None:
            print(f"st.session_state.uploaded_file is None 1")
            uploaded_file = st.file_uploader("Choose a graph JSON file", type="json")
            # If a new file is uploaded, save it to session state
            if uploaded_file is not None:
                print(f"Selected file {uploaded_file}")
                st.session_state.uploaded_file = uploaded_file
            else:
                print(f"uploaded_file is none so st.session_state.uploaded_file is None 2")
        if st.session_state.uploaded_file is not None:
            try:
                print(f"Querying {uploaded_file} from session state")
                uploaded_file = st.session_state.uploaded_file
                # # Read the file content directly
                # file_content = uploaded_file.read()
                # # Parse the JSON data
                # json_data = json.loads(file_content)

                # Import the data using the IntegratedGraphManager
                # nodes, edges = st.session_state.graph_obj.import_data(json_data)
                print(f"Importing from {uploaded_file}")
                graph_data = json.load(uploaded_file)
                nodes, edges = st.session_state.graph_obj.import_data(graph_data)
                st.success("Graph imported successfully!")
                st.write(f"Imported {nodes} nodes and {edges} edges")
            except json.JSONDecodeError:
                st.error("Invalid JSON file. Please upload a valid JSON file.")
            except Exception as e:
                st.error(f"Failed to import graph: {str(e)}")
            else:
                st.write("Upload a graph JSON file to view or modify the graph.")

                # Optionally include other functionalities, like graph export, visualization, etc.
                st.write("Uploaded file:", st.session_state.uploaded_file.name)
                # Graph Visualization
                st.header("Graph Visualization")
                net = st.session_state.graph_obj.visualize_by_pyvis()
                with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmpfile:
                    net.save_graph(tmpfile.name)
                    with open(tmpfile.name, 'r', encoding='utf-8') as f:
                        components.html(f.read(), height=600)

                # SPARQL Query Interface
                st.header("SPARQL Query")
                query = st.text_area("Enter SPARQL Query")
                if st.button("Execute Query"):
                    results = st.session_state.graph_obj.sparql_query(query)
                    st.write(results.serialize(format="json"))

                # Export functionality
                st.header("Export Graph")
                if st.button("Export Graph"):
                    nx_graph = st.session_state.graph_obj.export_to_networkx()
                    st.download_button(
                        label="Download NetworkX Graph",
                        data=json.dumps(nx.node_link_data(nx_graph)),
                        file_name="graph_data.json",
                        mime="application/json"
                    )

    # JavaScript callback for node/edge selection
    st.markdown("""
    <script>
    function selectElement(elementType, elementId) {
        const data = {
            element_type: elementType,
            element_id: elementId
        };
        window.parent.postMessage(JSON.stringify(data), "*");
    }
    </script>
    """, unsafe_allow_html=True)

    # Handle the selection message from JavaScript
    if st.session_state.selected_element is None:
        st.session_state.selected_element = None

    def handle_selection(data):
        st.session_state.selected_element = (data['element_type'], data['element_id'])
        st.experimental_rerun()

    st.markdown("""
    <script>
    window.addEventListener('message', function(event) {
        const data = JSON.parse(event.data);
        window.Streamlit.setComponentValue(data);
    });
    </script>
    """, unsafe_allow_html=True)

    # Use a container to trigger rerun on selection
    placeholder = st.empty()
    selection = placeholder.text_input("Selected Element", key="selection_input", label_visibility="hidden")
    if selection:
        data = json.loads(selection)
        st.session_state.selected_element = (data['element_type'], data['element_id'])
        placeholder.empty()
        st.experimental_rerun()


if __name__ == "__main__":
    main_ui()
