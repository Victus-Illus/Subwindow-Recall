<html>
<h1>Subwindow Recall</h1>
<p>A plugin that recalls subwindows layouts</p>
<h2>What does it do?</h2>
<p>Subwindow Recall saves the sizes and positions of subwindows in a file, which is then able
to recall them, so you don’t have to manually reposition your subwindows every time you open a document.</p>
    
<h2>How to Use</h2>
<ol>
	<li>Enable <strong>"Save Subwindows Layout"</strong> in <code>Tools > Scripts</code>.</li>
	<li>Save your document to create a save file of the current subwindows layout
	<li>Load a saved layout anytime using <strong>"Load Subwindows Layout"</strong> in <code>Tools > Scripts</code>.</li>
	<li>(Optional) Set up shortcuts for quicker access.</li>
</ol>
<h3>Tips</h3>
<ul>
	<li>It is recommended setting a shortcut for <strong>"Load Subwindows Layout"</strong>, as it is the one you will be using the most.</li>
	<li>This plugin works best in conjunction with Krita Sessions, which can be acessed by <code>File > Sessions</code>. That saves you the time of manually opening the right amount of subwindows</li>
	<li>You are able to reuse layouts in different works, all you have to do is copy the .txt file of the layout you wish to reuse, paste it in the same folder as the .kra file, and rename it to same name as that file (<code>drawing 2.kra > drawing 2.txt</code>)
	<li>A backup file of the current layout is always created whenever you save, with the extension .txt~, to enable it, all you have to do is remove the <strong>"~"</strong></li> 
</ul>
 
<h2>Requirements</h2>
<ol>
	<li><strong> "Subwindow"</strong> is enabled in <code>Settings > Configure Krita > General > Window > Multiple Document Mode</code>.</li>
	<li>the amount of subwindows must be equal to the amount of when you last saved your document, otherwise a new save will be requested.</li>
</ol>

<h2>Installation</h2>
<ol>
	<li>Download the ZIP file from the most recent <a href="https://github.com/Victus-Illus/Subwindow-Recall/releases">release</a>.</li>
	<li>Follow <a href="https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html">this guide</a> to install the plugin.</li>
	<li>To enable shortcuts, follow the <strong>manual installation</strong> steps (if the actions folder does not exist, you can simply create it).</li>
</ol>
 </html>
