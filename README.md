<p>This is a url to urn converter script named WebScraber for project FragTrag (https://fragtrag1.upatras.gr/exist/apps/fragtrag/index.html).</p>
<p>This is only a pre-release of the final version and there is more things to be done.</p>
<p>One of the project's main objectives is to describe the algorithm for the creation of urns contained in platform FragTrag.</p>
<p><figure><img src="Docs/ssht-01.png" alt="Array screenshot from debugger" title="Array screenshot from debugger"><figcaption>Links array screenshot from debugger</figcaption></figure></p>
<p>The script creates a two dimensional array (links_array) which contains required information for implimenting FragTrag urns, an array of all the urls (urls_array) to be interpreted and an array of the urns (urns_array) exported by the script. Each extracted link (url) is seperated in seven [7] elements that describe the content to which the link refers. These elements are used in composing the final list of urns exported as a text file with the name <a href="Docs/urns.txt" target="_blank">urns.txt</a>.</p>
<p><figure><img src="Docs/ssht-02.png" alt="Array screenshot from debugger" title="Array screenshot from debugger"><figcaption>Urns array screenshot from debugger</figcaption></figure></p>
<h3>Links_array description</h3>
<p><strong>Array of links contains</strong></p>
    <p>[0]: Reference to eXist-db [The Open Source Native XML Database] (not required)</p>
    <p>[1]: Platform url attribute (not required)</p>
    <p>[2]: Platform name (not required)</p>
    <p>[3]: Name of poet (Required)</p>
    <p>[4]: Name of object (Required)</p>
    <p>[5]: Type of object or poem title (Optional)</p>
    <p>[6]: Source identifier (Optional)</p>
<p>### ToDo - urn path description ###</p>
<p>Additionaly a file with all the urls extracted be WebScraber is being created for future reference and debugging of resutls (A sample of the file exported can be found <a href="Docs/urls.txt" target="_blank">here</a>).</p>
<p>Moreover an attempt is being done to describe the algorithm behind which the urns are being created trying to build a standardized method.</p>
