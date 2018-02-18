Team Compass for JupyterHub and Binder
======================================

Weekly reports
--------------

The following reports keep track of activity in the JupyterHub community.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   weekly-reports/weekly_report_index
   monthly-meeting/monthly_report_index

Team activity across repositories
---------------------------------

This dashboard reflects many kinds of activity (PRs, issues, etc) across the
JupyterHub organization. `Here is the direct link <https://dashboard.cauldron.io/app/kibana#/dashboard/Overview?_g=(filters:!(('$$hashKey':'object:78','$state':(store:globalState),meta:(alias:!n,disabled:!f,index:git,key:project,negate:!f,value:jupyterhub),query:(match:(project:(query:jupyterhub,type:phrase))))),refreshInterval:(display:Off,pause:!f,value:0),time:(from:now-3M,mode:relative,to:now))&_a=(filters:!(),options:(darkTheme:!f),panels:!((col:10,id:GitGithubRepos,panelIndex:2,row:5,size_x:3,size_y:5,title:'Top+Repositories',type:visualization),(col:1,id:github_authors_map,panelIndex:13,row:10,size_x:6,size_y:7,title:'Submitters+(Issues+%26+Pull+Requests)',type:visualization),(col:4,id:gitgithub_evolution_authors,panelIndex:14,row:8,size_x:3,size_y:2,title:Authors,type:visualization),(col:1,id:gitgithub_git_authors,panelIndex:16,row:6,size_x:3,size_y:4,title:'Top+Authors',type:visualization),(col:4,id:github_issues_evolutionary,panelIndex:17,row:2,size_x:6,size_y:2,title:Issues,type:visualization),(col:4,id:github_pullrequests_pullrequests,panelIndex:18,row:4,size_x:6,size_y:2,title:'Pull+Request',type:visualization),(col:4,id:git_evolution_commits,panelIndex:19,row:6,size_x:3,size_y:2,title:Commits,type:visualization),(col:7,id:git_commits_timezone,panelIndex:20,row:8,size_x:3,size_y:2,title:'Commits+by+Timezone',type:visualization),(col:7,id:github_assignees_map,panelIndex:21,row:10,size_x:6,size_y:7,title:'Assignees+(Issues+%26+Pull+Requests)',type:visualization),(col:10,id:gitgithub_domains,panelIndex:23,row:2,size_x:3,size_y:3,title:Domains,type:visualization),(col:7,id:git_added_vs_removed_lines,panelIndex:24,row:6,size_x:3,size_y:2,title:'Added+Vs+Removed+Lines',type:visualization),(col:1,id:github_issues_pull_requests_authors,panelIndex:25,row:2,size_x:3,size_y:4,title:'Top+Submitters+(Issues+%26+PRs)',type:visualization),(col:1,id:overview_doc,panelIndex:26,row:1,size_x:12,size_y:1,title:'Welcome!!',type:visualization)),query:(query_string:(analyze_wildcard:!t,query:'*')),title:Overview,uiState:(P-13:(mapCenter:!(14.604847155053898,0.3515625),title:'Submitters+(Issues+%26+Pull+Requests)'),P-14:(title:Authors,vis:(legendOpen:!f)),P-16:(title:'Top+Authors',vis:(params:(sort:(columnIndex:!n,direction:!n)))),P-17:(title:Issues),P-18:(title:'Pull+Request'),P-19:(title:Commits,vis:(legendOpen:!f)),P-2:(title:'Top+Repositories',vis:(params:(sort:(columnIndex:!n,direction:!n)))),P-20:(title:'Commits+by+Timezone',vis:(legendOpen:!f)),P-21:(mapCenter:!(9.44906182688142,0.3515625),spy:(mode:(fill:!f,name:!n)),title:'Assignees+(Issues+%26+Pull+Requests)'),P-23:(title:Domains),P-24:(title:'Added+Vs+Removed+Lines',vis:(legendOpen:!f)),P-25:(title:'Top+Submitters+(Issues+%26+PRs)',vis:(params:(sort:(columnIndex:!n,direction:!n)))),P-26:(title:'Welcome!!')))>`_
to the Cauldron dashboard displayed below. 

.. raw:: html

   <iframe src="https://dashboard.cauldron.io/app/kibana#/dashboard/Overview?embed=true&_g=(filters:!(('$state':(store:globalState),meta:(alias:!n,disabled:!f,index:git,key:project,negate:!f,value:jupyterhub),query:(match:(project:(query:jupyterhub,type:phrase))))),time:(from:now-3M,mode:quick,to:now))&_a=(filters:!(),options:(darkTheme:!f),panels:!((col:10,id:GitGithubRepos,panelIndex:2,row:5,size_x:3,size_y:5,title:'Top+Repositories',type:visualization),(col:1,id:github_authors_map,panelIndex:13,row:10,size_x:6,size_y:7,title:'Submitters+(Issues+%26+Pull+Requests)',type:visualization),(col:4,id:gitgithub_evolution_authors,panelIndex:14,row:8,size_x:3,size_y:2,title:Authors,type:visualization),(col:1,id:gitgithub_git_authors,panelIndex:16,row:6,size_x:3,size_y:4,title:'Top+Authors',type:visualization),(col:4,id:github_issues_evolutionary,panelIndex:17,row:2,size_x:6,size_y:2,title:Issues,type:visualization),(col:4,id:github_pullrequests_pullrequests,panelIndex:18,row:4,size_x:6,size_y:2,title:'Pull+Request',type:visualization),(col:4,id:git_evolution_commits,panelIndex:19,row:6,size_x:3,size_y:2,title:Commits,type:visualization),(col:7,id:git_commits_timezone,panelIndex:20,row:8,size_x:3,size_y:2,title:'Commits+by+Timezone',type:visualization),(col:7,id:github_assignees_map,panelIndex:21,row:10,size_x:6,size_y:7,title:'Assignees+(Issues+%26+Pull+Requests)',type:visualization),(col:10,id:gitgithub_domains,panelIndex:23,row:2,size_x:3,size_y:3,title:Domains,type:visualization),(col:7,id:git_added_vs_removed_lines,panelIndex:24,row:6,size_x:3,size_y:2,title:'Added+Vs+Removed+Lines',type:visualization),(col:1,id:github_issues_pull_requests_authors,panelIndex:25,row:2,size_x:3,size_y:4,title:'Top+Submitters+(Issues+%26+PRs)',type:visualization),(col:1,id:overview_doc,panelIndex:26,row:1,size_x:12,size_y:1,title:'Welcome!!',type:visualization)),query:(query_string:(analyze_wildcard:!t,query:'*')),title:Overview,uiState:(P-13:(mapCenter:!(14.604847155053898,0),title:'Submitters+(Issues+%26+Pull+Requests)'),P-14:(title:Authors,vis:(legendOpen:!f)),P-16:(title:'Top+Authors',vis:(params:(sort:(columnIndex:!n,direction:!n)))),P-17:(title:Issues),P-18:(title:'Pull+Request'),P-19:(title:Commits,vis:(legendOpen:!f)),P-2:(title:'Top+Repositories',vis:(params:(sort:(columnIndex:!n,direction:!n)))),P-20:(title:'Commits+by+Timezone',vis:(legendOpen:!f)),P-21:(mapCenter:!(9.44906182688142,0),title:'Assignees+(Issues+%26+Pull+Requests)'),P-23:(title:Domains),P-24:(title:'Added+Vs+Removed+Lines',vis:(legendOpen:!f)),P-25:(title:'Top+Submitters+(Issues+%26+PRs)',vis:(params:(sort:(columnIndex:!n,direction:!n)))),P-26:(title:'Welcome!!')))" height="600" width="800"></iframe>

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
