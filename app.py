import streamlit as st
import pdf2image
import os
import fitz
import pandas as pd


# main function
def main():
    st.title("SLR Parser")
    st.subheader("Enter Grammer and Token")
    grammer = st.text_area("Enter Grammer", height=200)
    token = st.text_area("Enter Token", height=200)
    if st.button("Parse"):
        with open('test_grammer.txt', 'w') as f:
            f.write(grammer)
        bashCommand = f"python slr.py -g test_grammer.txt {token}"
        os.system(bashCommand)
        st.success("Parsing Done")
        st.write("Augmented Grammer")
        # read augmented grammer csv file
        df = pd.read_csv('augmented_grammar.csv')
        st.dataframe(df)
        # print terminals and non terminals in the grammer
        st.write("Terminals")
        terminals = pd.read_csv('terminals.csv')
        st.dataframe(terminals)
        st.write("Non Terminals")
        non_terminals = pd.read_csv('nonterminals.csv')
        st.dataframe(non_terminals)
        st.write("Symbols")
        symbols = pd.read_csv('symbols.csv')
        st.dataframe(symbols)

        # print first and follow sets
        st.write("First Sets")
        first_sets = pd.read_csv('first.csv')
        st.dataframe(first_sets)
        st.write("Follow Sets")
        follow_sets = pd.read_csv('follow.csv')
        st.dataframe(follow_sets)

        st.write("DFA Table")
        pdffile = "automaton.gv.pdf"
        doc = fitz.open(pdffile)
        page = doc.load_page(0) 
        pix = page.get_pixmap()
        output = "outfile.png"
        pix.save(output)
        st.image(output, use_column_width=True)


        # print parsing table
        st.write("Parsing Table")
        parsing_table = pd.read_csv('parse_table.csv')

        # replace nan with empty string
        parsing_table = parsing_table.fillna('')
        st.dataframe(parsing_table)


        st.write("Parsing Steps")
        parsing_steps = pd.read_csv('parsing_results.csv')
        parsing_steps = parsing_steps.fillna('')
        st.dataframe(parsing_steps)

        




if __name__ == "__main__":
    main()


        

