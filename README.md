<h1> AutoOpenApi <h1>

<p>
Is an attempt to automate the production of API documentation. 
This library attempts to build API documentation to OpenApi3 Specification.
</p>

<p>
It does this based on the tests defined, in your project. 
In order to generate your API documentation you need to do the following:
<ul>
    <li>1. Install the library
    <li>2. Put a <FILENAME>.yaml file in your tests/ dir
    <li>3. import the package: from AutoOpenApi.autoopenapi import ToDoc
    <li>4. include a call to build an endpoint in the tests you wish to have included: ToDoc(your_input_file, your_output_file).build_endpoint(event=your_event, response=your_response)
    <li>5. Run the tests
</ul>
<img src="image.png">
</p>