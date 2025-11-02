document.getElementById('upload-form').onsubmit = function(event) {
    event.preventDefault(); // Prevent the default form submission

    var form = document.getElementById('upload-form');
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();

    xhr.upload.addEventListener('progress', function(e) {
        if (e.lengthComputable) {
            var percentComplete = (e.loaded / e.total) * 100;
            var progressBar = document.getElementById('progress-bar');
            progressBar.style.width = percentComplete + '%';
            progressBar.textContent = Math.round(percentComplete) + '%';
        }
    });

    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            if (xhr.status == 200) {
                var progressBar = document.getElementById('progress-bar');
                progressBar.style.width = '100%';
                progressBar.textContent = 'Upload complete';

                // Display the processed filenames
                var response = JSON.parse(xhr.responseText);
                var message = document.getElementById('message');
                message.textContent = 'File processed: ' + response.filename;

                var downloadLinks = document.getElementById('download-links');
                downloadLinks.innerHTML = ''; // Clear existing links

                response.csv_files.forEach(function(csv_file) {
                    var link = document.createElement('a');
                    link.href = '/download/' + csv_file;
                    link.textContent = 'Download ' + csv_file;
                    link.classList.add('btn', 'btn-primary', 'm-2');
                    downloadLinks.appendChild(link);
                });

            } else {
                alert('An error occurred during the upload');
            }
        }
    };

    xhr.open('POST', form.action, true);
    xhr.send(formData);
};
