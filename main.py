from flask import Flask, render_template, request, redirect
from rrk import extract_rrk_jobs
from wwr import extract_wwr_jobs

app = Flask("job_scrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result")
def result():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    else:
        rrk = extract_rrk_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        results = rrk + wwr
    return render_template("result.html", keyword=keyword, results=results)


app.run("0.0.0.0")
