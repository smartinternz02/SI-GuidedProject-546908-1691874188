from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Replace these with your actual Tableau story and dashboard URLs
    tableau_story_url = "https://public.tableau.com/views/Complete_EV_Analysis_Story/EV_Story?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link"
    tableau_dashboard_url_1 = "https://public.tableau.com/views/Complete_EV_Analysis/Ev_Range_Analysis?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link"
    tableau_dashboard_url_2 = "https://public.tableau.com/views/Complete_EV_Analysis2/Ev_Range_Analysis2?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link"
    return render_template('dashboard.html', tableau_story_url=tableau_story_url, tableau_dashboard_url_1=tableau_dashboard_url_1, tableau_dashboard_url_2=tableau_dashboard_url_2)

if __name__ == '__main__':
    app.run(debug=True)
