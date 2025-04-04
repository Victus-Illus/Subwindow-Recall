<html>
<h1>Subwindow Recall</h1>
<p>A plugin that recalls subwindows layouts</p>
<h2>What does it do?</h2>
<p>Subwindow Recall saves the sizes and positions of subwindows in a file, which is then able
to recall them, so you don’t have to manually reposition your subwindows every time you open a document.</p>
    
<h2>How to Use</h2>
<ol>
	<li>Enable <strong>"Auto-save layouts"</strong> in <code>Tools > Scripts > SubwindowRecall</code>.</li>
	<li>Save your document to create a save file of the current subwindows layout
	<li>Load your last saved layout anytime using <strong>"Load Subwindows Layout"</strong> in <code>Tools > Scripts</code>.</li>
	<li>(Optional) Set up shortcuts for quicker access.</li>
</ol>
<h3>Tips</h3>
<ul>
	<li>It is recommended setting a shortcut for <strong>"Load Subwindow Layout"</strong>, as it is the one you will be using the most.</li>
	<li>Is it advised to set a layout directory in any place of your choosing, that allows you to save different layout setups and be able reuse them with ease, without creating duplicates of existing layouts, it can be set in <code>Tools > Scripts > SubwindowRecall > Set layout folder to...</code></li>
	<li>A backup file of the current layout is always created whenever you save, with the extension .txt~, to re-activate it, all you have to do is remove the ~</li>
	<li>Whenever you save your document, your current layout is saved, so if you use 'Load Subwindow Layout' in a different document, it will still load your last used layout</li>
	<li>To enable shortcuts, follow the <strong>manual installation</strong> steps from <a href="https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html">this guide</a> (if the actions folder does not exist, you can simply create it).</li>
	<li>If you have more or less windows than the amount necessary for the selected layout, they will be created or closed automatically</li>
</ul>
 
<h2>Requirements</h2>
<ol>
	<li><strong> "Subwindow"</strong> is enabled in <code>Settings > Configure Krita > General > Window > Multiple Document Mode</code>.</li>
</ol>

<h2>Installation</h2>
<ol>
	<li>Download the ZIP file from the most recent <a href="https://github.com/Victus-Illus/Subwindow-Recall/releases">release</a>.</li>
	<li>Follow <a href="https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html">this guide</a> to install the plugin.</li>
	<li>To enable shortcuts, follow the <strong>manual installation</strong> steps (if the actions folder does not exist, you can simply create it).</li>
</ol>
 </html>
