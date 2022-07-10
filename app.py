# Imports
from dash import Dash, dcc, html
import plotly.graph_objects as go
import database
import find
import webbrowser
db = database.DataBase()

# Call a the Google Forms API to get all the Data from the Survay
find.Update().refreshAPI()

# Startup Dash
app = Dash(__name__)



#----------------- Creating 'Pick a Number' Bar Chart -------------------------
countNum=db.getCountNum()
numLabel = [1,2,3,4,5,6,7,8,9,10]
data = [go.Bar(
x = numLabel,
y = countNum,
text=numLabel,
textfont_size=40,
hoverinfo='y'
)]
figNum = go.Figure(data=data)
figNum.update_layout(
    autosize=True,
    title_text="Pick a number",
    title_x=0.5,
    height=400,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
)
figNum.update_yaxes(ticklabelstep=1)
figNum.update_xaxes(showticklabels=False)



#----------------- Creating 'Pick a Color' Pie Chart -------------------------
colorCount=db.getCountCol()
z = colorCount
colLable = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Black']
countCol = [z['Red'], z['Orange'], z['Yellow'], z['Green'], z['Blue'], z['Purple'], z['Black']]
trace = go.Pie(labels = colLable, values = countCol, showlegend=False)
data = [trace]
figCol = go.Figure(data = data)
figCol.update_traces(hoverinfo='label+percent', textinfo='percent', textposition="inside", textfont_size=20,
                marker=dict(colors=colLable, line=dict(color='#000000', width=0)))
figCol.update_layout(
    autosize=False,
    title_text="Pick a Color",
    title_x=0.5,
    height=400,
    margin=dict(
        l=50,
        r=50,
        b=0,
        t=100,
        pad=4
    ),
)



#----------------- Creating 'Dogs or Cats' Bar Chart -------------------------
animalCount=db.getCountAni()
q = animalCount
aniLabel = ['Dogs', 'Cats']
countAni = [q['Dogs'], q['Cats']]
data = [go.Bar(
x = countAni,
y = aniLabel,
orientation='h',
text=['Dogs', 'Cats'],
textfont_size=40,
textposition="inside",
hoverinfo='text'
)]
figAni = go.Figure(data=data)
figAni.update_layout(
    autosize=False,
    title_text="Dogs or Cats",
    title_x=0.5,
    width=700,
    height=400,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
)
figAni.update_yaxes(showticklabels=False)


# Page Layout
def serve_layout():
    return html.Div([   
        html.Div(children=[
            dcc.Graph(id="animal-graph", figure=figAni ,style={'display': 'inline-block'}),
            dcc.Graph(id="color-graph", figure=figCol, style={'display': 'inline-block'}),
        ]),
        dcc.Graph(id="number-graph", figure=figNum)
        ])

app.layout = serve_layout

# Open Graph Page
webbrowser.open('http://127.0.0.1:8050') 

# Start Graphing
if __name__ == "__main__":
    app.run_server(debug=False)

