<html>
	<h1>Subwindow Recall</h1>
	<p>A plugin that recalls subwindows layouts</p>
	<h2>What does it do?</h2>
	<p>Subwindow Recall saves the sizes and positions of subwindows in a file, which is then able
   	to read that file to recall them, so that it can reproduce the layout of the subwindows previously set by the user. This saves you the trouble of having to manually set your subwindows sizes and positions every time you open a document.</p>
    
<h2>Usage</h2>
	<p>To use Subwindow Recall, all you need to do is enable 'Save Subwindow Layout' in Tools/Scripts, that will make so that the plugin starts creating save files of the subwindows layouts. Then, when you want to recall the layout, use the 'Load Subwindow Layout' in Tools/Scripts</p>
	<p>Shortcuts can be added for both actions.</p>
	<h3>Tips</h3>
 	<ul>
		<li>It is recommended setting a shortcut for 'Load Subwindow Layout', as it is the one you will be using the most.</li>
		<li>This plugin works best in conjunction with Krita Sessions, which can be acessed by File > Sessions. That saves you the time of manually opening the right amount of subwindows</li>
		<li>You are able to reuse layouts in different works, all you have to do is copy the .txt file of the layout you wish to reuse, paste it in the same folder/directory as the .kra file, and rename it to same name as that file (drawing 2.kra > drawing 2.txt)
		<li>A backup file of the current layout is always created whenever you save, with the extension .txt~, to re-activate it, all you have to do is remove the ~</li> 
	</ul>
 
<h2>Requirement</h2>
	<p>'subwindow' mode is enabled in Settings > Configure Krita > General > Window > Multiple Document Mode.</p>

<h2>Installation</h2>
	<p>To install this plugin, start by downloading it by clicking the green button 'Code' and pressing 'Download ZIP'</p>
 	<p> From there, you can follow this <a href="https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html">guide</a> on the Krita official site, to add the shortcuts, you need to follow the manual part of the guide, extracting the .zip file, and adding subwindowOrganizer.action to the actions in the actions folder, inside the resource folder.</p> 
  	<p>If the actions folder does not exist, you can just create it</p>

 </html>
