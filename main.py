import csv
import requests
# from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask, render_template, request, redirect
from markupsafe import escape


def write_data(data):
    if "\n" in data['message'] or "\r" in data['message']:
        data['message'] = data['message'].replace("\n", " ").replace("\r", " ").replace("  ", " ")
    with open('./database.csv', mode='a', newline='') as csvfile:
        email = escape(data['email'])
        subject = escape(data['subject'])
        message = escape(data['message'])
        writer = csv.writer(csvfile)
        writer.writerow([email, subject, message])


app = Flask(__name__)
# csrf = CSRFProtect(app)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
@app.route("/<string:page_name>")
def page(page_name='index.html'):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data(data)
            return redirect('./thankyou.html')
        except requests.exceptions.ConnectionError as err:
            print(err)
            raise ConnectionError("Failed to connect to the server") from err
    else:
        return 'Something went wrong.'


@app.context_processor
def inject_navigation_bar():
    html_data = """
      <nav class="navbar navbar-expand-lg fixed-top navbar-transparent" color-on-scroll="100">
        <div class="container">
          <div class="navbar-translate">
            <a class="navbar-brand" href="index.html" rel="tooltip" title="PORTFOLIO • Kirk Wallace" data-placement="bottom">
              <span>PORTFOLIO •</span> Kirk Wallace
            </a>
            <button class="navbar-toggler navbar-toggler" type="button" data-toggle="collapse" data-target="#navigation" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-bar bar1"></span>
              <span class="navbar-toggler-bar bar2"></span>
              <span class="navbar-toggler-bar bar3"></span>
            </button>
          </div>
          <div class="collapse navbar-collapse justify-content-end" id="navigation">
            <div class="navbar-collapse-header">
              <div class="row">
                <div class="col-6 collapse-brand">
                  <a>
                    PORTFOLIO • Kirk Wallace
                  </a>
                </div>
                <div class="col-6 collapse-close text-right">
                  <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navigation" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
                    <i class="tim-icons icon-simple-remove"></i>
                  </button>
                </div>
              </div>
            </div>
            <ul class="navbar-nav">
              <li class="nav-item p-0">
                <a class="nav-link" rel="tooltip" title="Follow me on Threads" data-placement="bottom" href="https://www.threads.net/@0xtrace" target="_blank">
                  <i class="fa-brands fa-square-threads"></i>
                  <p class="d-lg-none d-xl-none">Threads</p>
                </a>
              </li>
              <li class="nav-item p-0">
                <a class="nav-link" rel="tooltip" title="Follow me on X" data-placement="bottom" href="https://twitter.com/0xTrace" target="_blank">
                  <i class="fa-brands fa-square-x-twitter"></i>
                  <p class="d-lg-none d-xl-none">Twitter</p>
                </a>
              </li>
              <li class="nav-item p-0">
                <a class="nav-link" rel="tooltip" title="Follow me on LinkedIn" data-placement="bottom" href="https://www.linkedin.com/in/rkwallacejr/" target="_blank">
                  <i class="fa-brands fa-linkedin"></i>
                  <p class="d-lg-none d-xl-none">LinkedIn</p>
                </a>
              </li>
              <li class="nav-item p-0">
                <a class="nav-link" rel="tooltip" title="Follow me on Instagram" data-placement="bottom" href="https://www.instagram.com/0xtrace/" target="_blank">
                  <i class="fa-brands fa-instagram"></i>
                  <p class="d-lg-none d-xl-none">Instagram</p>
                </a>
              </li>
              <li class="dropdown nav-item">
                <a href="#" class="dropdown-toggle nav-link" data-toggle="dropdown">
                  <i class="fa fa-cogs d-lg-none d-xl-none"></i> Navigation
                </a>
                <div class="dropdown-menu dropdown-with-icons">
                  <a href="projects.html" class="dropdown-item">
                    <i class="tim-icons icon-paper"></i> Projects
                  </a>
                  <a href="profile-page.html" class="dropdown-item">
                    <i class="tim-icons icon-single-02"></i>Profile Page
                  </a>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    """
    return {"html_navigation_bar": html_data}


@app.context_processor
def inject_header():
    html_data = """
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <link
      rel="apple-touch-icon"
      sizes="76x76"
      href="./static/assets/img/apple-icon.png"
    />
    <link rel="icon" type="image/png" href="./static/assets/img/favicon.png" />
    <title>Portfolio • Kirk Wallace</title>
    <!--     Fonts and icons     -->
    <link
      href="https://fonts.googleapis.com/css?family=Poppins:200,300,400,600,700,800"
      rel="stylesheet"
    />
    <!-- Nucleo Icons -->
    <link href="./static/assets/css/nucleo-icons.css" rel="stylesheet" />
    <!-- CSS Files -->
    <link
      href="./static/assets/css/blk-design-system.css?v=1.0.0"
      rel="stylesheet"
    />
    """
    return {"html_head": html_data}


@app.context_processor
def inject_footer():
    html_data = """
          <footer class="footer">
            <div class="container">
              <div class="row">
                <div class="col-md-3">
                  <h1 class="title">K • W</h1>
                </div>
                <div class="col-md-3">
                  <ul class="nav">
                    <li class="nav-item">
                      <a href="/index.html" class="nav-link"> Home </a>
                    </li>
                    <li class="nav-item">
                      <a href="/projects.html" class="nav-link">
                        Projects
                      </a>
                    </li>
                    <li class="nav-item">
                      <a href="/profile-page.html" class="nav-link">
                        About Me
                      </a>
                    </li>
                  </ul>
                </div>
                <div class="col-md-3">
                  &nbsp;
                </div>
                <div class="col-md-3">
                  &nbsp;
                </div>
              </div>
            </div>
          </div>
        </footer>
      </div>
            <!--   Core JS Files   -->
            <script
              src="./static/assets/js/core/jquery.min.js"
              type="text/javascript"
            ></script>
            <script
              src="./static/assets/js/core/popper.min.js"
              type="text/javascript"
            ></script>
            <script
              src="./static/assets/js/core/bootstrap.min.js"
              type="text/javascript"
            ></script>
            <script src="./static/assets/js/plugins/perfect-scrollbar.jquery.min.js"></script>
            <script
              src="https://kit.fontawesome.com/f000b2613b.js"
              crossorigin="anonymous"
            ></script>
            <!--  Plugin for Switches, full documentation here: http://www.jque.re/plugins/version3/bootstrap.switch/ -->
            <script src="./static/assets/js/plugins/bootstrap-switch.js"></script>
            <!--  Plugin for the Sliders, full documentation here: http://refreshless.com/nouislider/ -->
            <script
              src="./static/assets/js/plugins/nouislider.min.js"
              type="text/javascript"
            ></script>
            <!-- Chart JS -->
            <script src="./static/assets/js/plugins/chartjs.min.js"></script>
            <!--  Plugin for the DatePicker, full documentation here: https://github.com/uxsolutions/bootstrap-datepicker -->
            <script src="./static/assets/js/plugins/moment.min.js"></script>
            <script
              src="./static/assets/js/plugins/bootstrap-datetimepicker.js"
              type="text/javascript"
            ></script>
            <!-- Control Center for Black UI Kit: parallax effects, scripts for the example pages etc -->
            <script
              src="./static/assets/js/blk-design-system.min.js?v=1.0.0"
              type="text/javascript"
            ></script>
    """
    return {"html_footer": html_data}


# @app.after_request
# def set_csrf_cookie(response):
#     response.set_cookie('csrf_token', generate_csrf())
#     return response
