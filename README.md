<html>
<h1>Subwindow Recall</h1>
<p>A plugin that recalls subwindows layouts</p>
<h2>What does it do?</h2>
<p>Subwindow Recall saves the sizes and positions of subwindows in a file, which is then able
to recall them, so you don’t have to manually reposition your subwindows every time you open a document.</p>
    
<h2>How to Use</h2>
<ol>
	<li>Enable <strong>"Auto-save layouts"</strong> in <code>Tools > Scripts > Subwindow Recall</code>.</li>
	<li>Save your document to create a save file of the current subwindows layout
	<li>Load your last saved layout anytime using <strong>"Load current Layout"</strong> in <code>Tools > Scripts > Subwindow Recall</code>.</li>
	<li>(Optional) Set up shortcuts for quicker access.</li>
</ol>

<h2>Menu</h2>
<h3>A explanation of what it does and how can it help <strong>you</strong> improve your workflow</h3>
<p>The menu is a new window that you can open from <code>Tools > Scripts > Subwindow Menu</code>, it was designed to look similar to the Sessions window to keep a consistent design across the app.</p>
<h3>The menu has the following actions</h3>

<ol>
    <li>Auto-save layout</li>
    <p>Formerly known as "Save Subwindows Layout", it still works the same way as it did before, it was moved to the menu, to avoid filling the <code> Tools > Scripts</code> with too many actions from Subwindow Recall. The shortcut for it has been removed, as it would likely lead to accidents by not giving feedback when it's toggled or not without opening the menu.</p>
    <li>Save current layout as...</li>
    <p>Saves the current layout you are using right now as a separate file in any folder of your choosing, it's just like the Save As function for documents.</p>
    <li>Load current layout</li>
    <p>Formerly know as "Load Subwindows Layout", it does the same thing it did before with the bonus that it creates or closes subwindows to fit the layout automatically, it always loads the layout that you had when you last saved a document. The shortcut still works.</p>
    <li>Load selected layout</li>
    <p>Load the currently selected layout from the list of layouts in your layout folder.</p>
    <li>Search layout...</li>
    <p>Opens a window for you to search for a layout that is not inside the layout folder.</p>
    <li>Rename layout</li>
    <p>Rename the currently selected layout, you do <strong>NOT</strong> need to add .txt at the end, the menu will handle it.</p>
    <li>Delete selected layout</li>
    <p>Delete the currently selected layout, it will ask for your confirmation before deleting (the deleted layout does not go to your trash bin).</p>
    <li>Set layout folder to...</li>
    <p>Opens a window for you to choose your layout folder, it will then refresh the visible layouts to search for any in the choosen folder.</p>
</ol>
<h3>Tips</h3>
<ul>
	<li>It is highly <strong>recommended</strong> to set your layout folder!</li>
	<li>It is recommended setting a shortcut for <strong>"Load Current Layout"</strong>, as it is the one you will be using the most.</li>
	<li>Is it advised to set a layout directory in any place of your choosing, that allows you to save different layout setups and be able reuse them with ease, without creating duplicates of existing layouts, it can be set in <code>Tools > Scripts > SubwindowRecall > Set layout folder to...</code></li>
	<li>A backup file of the current layout is always created whenever you save, with the extension .txt~, to re-enable it, all you have to do is remove the ~</li>
	<li>Whenever you save your document, your current layout is saved, so if you use "Load current layout" in a different document, it will still load your last used layout, without the need to select it in the menu</li>
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
