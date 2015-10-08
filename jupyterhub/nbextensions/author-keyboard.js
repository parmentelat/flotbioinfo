// This is a rewrite of my previous devel_custom.js (that was for python2s1)
// for adding a few convenience keyboard shortcuts in jupyter (for bioinfo)
// how to do this is based on this page here
// https://carreau.gitbooks.io/jupyter-book/content/notebook-extensions.html
//
define(['base/js/namespace'],
       function(IPython){
	   function _on_load(){
	       
	       // ctrl-m / ctrl-u = move cell up
	       IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-u', {
		   help: 'Move cell up',
		   handler: function (event) {
		       IPython.notebook.move_cell_up();
		       return false;
		   }
	       });
	       
	       // ctrl-m / ctrl-d = move cell down
	       IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-d', {
		   help: 'Move cell down',
		   handler: function (event) {
		       IPython.notebook.move_cell_down();
		       return false;
		   }
	       });
	       
	       // also support ctrl-m ctrl-s in addition to ctrl-m s
	       IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-s', {
		   help: 'save notebook',
		   handler: function (event) {
		       IPython.notebook.save_notebook();
		       return false;
		   }
	       });

	       // ctrl-m ctrl-x like ctrl-m x : delete cell
	       IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-x', {
		   help: 'Delete current cell',
		   handler: function(envent) {
		       IPython.notebook.delete_cell();
		       return false;
		   }
	       });
	       // ctrl-m ctrl-c : clear all output
	       IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-c', {
		   help: 'Clear all output',                  
		   handler: function (event) {                
		       IPython.notebook.clear_all_output();   
		       return false;                          
		   }
	       });

	       // ctrl-m ctrl-0 : restart kernel - no question asked
	       IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-0', {
		   help: 'Restart kernel - no question asked',
		   handler: function (event) {
		       IPython.notebook.kernel.restart();
		       return false;
		   }
	       });

	       // ctrl-m ctrl-a : run all cells
	       IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-a', {
		   help: 'Run all cells',
		   handler: function (event) {
		       IPython.notebook.execute_all_cells();
		       return false;
		   }
	       });

	       // ctrl-m ctrl-f : full monty
	       var clear_restart_rerun_action = {
		   help: "Clear all cells, restart kernel, run all cells again",
		   /* tried stuff like 'fa-battery-full' 'fa-television' 'fa-hourglass' */
		   /* not working, jupyter seems to have 4.2 */
		   icon: 'fa-lightbulb-o',
		   help_index: '',
		   handler: function(env) {
		       var on_success = function(){
// based on this page https://carreau.gitbooks.io/jupyter-book/content/notebook-extensions.html
// which right now says it's not the right way (wait 1 sec, todo listen on Kernel ready event.)
			   setTimeout(function(){console.log("Running all cells");
						 env.notebook.execute_all_cells();
						},
				      1000);
		       };
		       var on_error = function(){
			   console.log("Something went wrong when restarting kernel");
		       };
		       env.notebook.clear_all_output();
		       env.notebook.kernel.restart(on_success, on_error);
		   }
	       };
	       IPython.keyboard_manager.command_shortcuts.add_shortcut(
		   'ctrl-f', clear_restart_rerun_action);
	       IPython.keyboard_manager.actions.register(
		   clear_restart_rerun_action, 'clear_restart_rerun', 'author-keyboard');

	       // ctrl-m ctrl-m : clear all output and save
	       var clear_save_action = {
		   help: "Clear all outputs and save",
		   icon: 'fa-save',
		   help_index: '',
		   handler: function(env) {
		       env.notebook.clear_all_output();
		       env.notebook.save_notebook();
		   }
	       };
	       IPython.keyboard_manager.command_shortcuts.add_shortcut(
		   'ctrl-m', clear_save_action);
	       IPython.keyboard_manager.actions.register(
		   clear_save_action, 'clear_save','author-keyboard');

	       IPython.toolbar.add_buttons_group([
		   'author-keyboard.clear_restart_rerun',
		   'author-keyboard.clear_save',
	       ]);
	    // A small hint so we can see through firebug that our custom code executed
	    console.log("Extension author-keyboard loaded");
	    
	}

	return {load_ipython_extension: _on_load};
    }
)
