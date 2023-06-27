######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Page Title
######################
st.set_page_config(layout="wide")

with st.container():
    st.write("""
    # DNA Nucleotide Count Web App

    This app counts the nucleotide composition of query DNA!

    ***
    """)


with st.container():
    container_2_col1, _, container_2_col2 = st.columns([.5, .1, .4])
    with container_2_col1:
        st.markdown("### Enter DNA sequence")
        sequence_input = """GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG"""

        #sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
        sequence = st.text_area("Sequence input", sequence_input, height=250)






sequence = sequence.splitlines()
sequence = ''.join(sequence) # Concatenates list to string

st.markdown("***")

## Prints the input DNA sequence

keys = []
for key in set(sequence):
    if key not in ['T', 'A', 'G', 'C']:
        keys.append(key)

if len(keys) > 0:
    texto = f'The input contains characters ({", ".join(keys)}) that are not identified as nucleotides. These characters were ignored.'
    st.warning(texto, icon="⚠️")

st.markdown("### Filtered input")
sequence


def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})

p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    # width=alt.Step(80)  # controls width of bar.
    width=600,
)

with container_2_col2:
    st.write(p)

df["%"] = df['count']*100/df['count'].sum()
df["%"] = df["%"].round(2)

st.markdown("### Summary")
st.dataframe(data=df, width=None, height=None, use_container_width=False, hide_index=True, column_order=None, column_config=None)
