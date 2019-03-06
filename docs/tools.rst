=====================
JupyterHub Team Tools
=====================

There are a few tools that the JupyterHub community uses to help make life
a bit better. This page contains some links and descriptions of each.

Add a button to the built documentation in a Pull Request
=========================================================

While most of the JupyterHub repositories use ReadTheDocs to host their
documentation, many also use CircleCI to build a **preview of documentation**
from the changes in a pull request. Once the Circle job has finished, this
can be accessed by clicking **details** next to the CircleCI job for the docs,
then clicking **Artifacts**, then clicking the HTML file you'd like to preview.

To make this easier, there is a short Javascript script that can add a button
to your PR page that takes you directly to the documentation for this PR. You
can use it in your browser by adding it with either `Greasemonkey <https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/>`_
(for Firefox) or `Tampermonkey <https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en>`_
(for Chrome).

Below is the text of the script. After you've initialized it in one of these
extensions, visiting the page of a PR that has a CircleCI job will
automatically show a button to take you to the documentation. Note that
you may need to reload the browser page to ensure the javascript is run.

.. code-block:: javascript

   // ==UserScript==
   // @name        see PR doc on CircleCI
   // @namespace   github.com
   // @include     /https://github.com/.*/pull/[0-9]+[^/]*$/
   // @grant       none
   // ==/UserScript==

   // Add a button to easily access HTML generated documentation on CircleCI
   (function(){
       'use strict';

       // First get the repository name for this project
       var repo = document.URL.split('github.com/')[1].split('/', 2)[1]

       // There is a unique number for each CircleCI project
       const CIRCLECI_PROJ_NUMBERS = {
           "zero-to-jupyterhub-k8s": "87849371",
           "repo2docker": "90722372",
           "binderhub": "89419368",
           "team-compass": "113493831",
           "binder": "100564515",
           "alabaster-jupyterhub": "153355305"
       }

       const CIRCLECI_NUM = CIRCLECI_PROJ_NUMBERS[repo];
       if (CIRCLECI_NUM === undefined) {
           console.log("CircleCI number for " + repo + " was not found");
           return
       }
       const BUTTON_TEXT = "Preview Built Docs";


       // Add buttons upon startup
       window.addEventListener('load', () => {
           var link = getCircleArtifactLink();
           addButton(BUTTON_TEXT, link);
       });

       function addButton(text, link, cssObj) {
           // Create a link to the built docs
           let buttonLink = document.createElement('a');
           buttonLink.href = link;

           // Add the button underneath the link
           let headerActionElement = document.getElementsByClassName('gh-header-actions')[0];
           cssObj = cssObj || {};
           let button = document.createElement('button'), btnStyle = button.style;
           button.innerHTML = text;
           button.classList = "btn btn-sm";
           button.type = "button";
           Object.keys(cssObj).forEach(key => btnStyle[key] = cssObj[key]);

           // Append the button to the link, and the link to the header
           buttonLink.appendChild(button)
           headerActionElement.appendChild(buttonLink);
           return button;
       }

       function getCircleArtifactLink() {
           var circleElement;
           var useCircleWorkflow;
           const jobSelectorText = "div.merge-status-item a.status-actions"

           if (circleElement !== undefined) {
               return;
           }

           // Find all elements for build jobs
           var elements = document.querySelectorAll(jobSelectorText);

           // Return elements that have circleci in the text
           // querySelector will return a NodeList so this treats it as an array
           var circleElements = Array.prototype.filter.call(elements, function(element){
               return (element.href.indexOf("circleci.com") !== -1);
           });
           // circleElements should be a list of length 1 so we'll just take the first element
           circleElement = circleElements[0]

           // Split up the circleElement's href into parts so we can grab the build number (will be last element in linkParts)
           var linkParts = circleElement.href.split('?')[0].split('/')
           var circleBuildNumber = linkParts[linkParts.length - 1];
           var docURLPart = '-'+CIRCLECI_NUM+'-gh.circle-artifacts.com/0/html';
           var docURL = 'https://' + circleBuildNumber + docURLPart + '/index.html';

           return docURL;
       }
   }());
