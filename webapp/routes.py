def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=0)
    config.add_route('home', '/')
    config.add_route('No_entry', '/result/noentry/{item}')
    config.add_route('api', '/api')
    config.add_route('api_filter', '/api/{column}/{filter}/{filter_value}')
    config.add_route('api_column', '/api/{column}')
    config.add_route('dashboard', '/dashboard')
    config.add_route('mlvaquery', '/mlvaquery')
    config.add_route('mstquery', '/mstquery')
    config.add_route('primerquery', '/primer')
    config.add_route('primerquery_results', '/primer_results/*selection')
    config.add_route('mlvaanalysis', '/mlvaanalysis')
    config.add_route('mlvaresult', '/mlvaresult')
    config.add_route('resMLVA', '/mlvaresult/{ID}')
    config.add_route('subMLVA', '/submissions/{ID}')
    config.add_route('phlMLVA', '/mlvaphyloanalysis/{ID}')
    config.add_route('coxviewer', '/coxviewer')
    config.add_route('api_coxviewer', '/coxviewer_api')
    config.add_route('api_coxviewer2', '/coxviewer_api/{ID}')
    config.add_route('coxviewer_table', '/coxviewer_table/{ID}')
    config.add_route('detailed_view', '/view/{ID}')
    config.add_route('mst_isolate_view', '/mst_isolate/{ID}')
    config.add_route('fp_query_api', '/fp_query/{ms01}/{ms03}/{ms20}/{ms21}/{ms22}/{ms23}/{ms24}/{ms26}/{ms27}/{ms28}/{ms30}/{ms31}/{ms33}/{ms34}')
    config.add_route('mst_query_api', '/mst_query/{COX2}/{COX5}/{COX18}/{COX20}/{COX22}/{COX37}/{COX51}/{COX56}/{COX57}/{COX61}')
    config.add_route('api_map', '/api_map/{column}/{state}')
    config.add_route('api_view_map', '/api_view_map/{ID}')
    config.add_route('api_query3', '/api_query/{ms24}/{ms28}/{ms33}')
    config.add_route('api_query6', '/api_query/{ms23}/{ms24}/{ms27}{ms28}/{ms33}/{ms34}')
    config.add_route('api_query141', '/api_query/{ms01}/{ms03}/{ms07}/{ms20}/{ms21}/{ms22}/{ms24}/{ms26}/{ms27}/{ms28}/{ms30}/{ms31}/{ms33}/{ms34}')
    config.add_route('api_query15', '/api_query/{ms01}/{ms03}/{ms07}/{ms12}/{ms20}/{ms21}/{ms22}/{ms24}/{ms26}/{ms27}/{ms28}/{ms30}/{ms31}/{ms33}/{ms34}')
    config.add_route('api_query16', '/api_query/{ms01}/{ms03}/{ms07}/{ms12}/{ms20}/{ms21}/{ms22}/{ms24}/{ms26}/{ms27}/{ms28}/{ms30}/{ms31}/{ms33}/{ms34}/{ms36}')

