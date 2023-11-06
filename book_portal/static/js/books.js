/*document.addEventListener("DOMContentLoaded", function() {
    const replyButtons = document.querySelectorAll(".reply-button");

    replyButtons.forEach(button => {
        button.addEventListener("click", function() {
            const commentId = this.getAttribute("data-comment-id");
            const replyForm = document.querySelector(`.reply-form[data-comment-id="${commentId}"]`);
            replyForm.style.display = replyForm.style.display === "none" ? "block" : "none";
        });
    });
})

function fetchData(replyId) {
    return new Promise((resolve, reject) => {
        fetch('/books/comment/'+replyId+'/getreplies')
            .then(response => response.json())
            .then(data => {
                // Process and use the JSON data as needed
                console.log(data);
                data.forEach(replyData => {
                    console.log(replyData)
                    const replyElement = document.createElement("div");
                    replyElement.className = "sample-reply";
                    replyElement.innerHTML = `
                        <div class="user-profile"></div>
                        <span class="user-name">${replyData.username}:</span> ${replyData.text}`;
                    replies.appendChild(replyElement);
                });

                // Resolve the Promise with the data
                resolve(data);
            })
            .catch(error => {
                console.error('An error occurred:', error);
                reject(error);
            });
    });
}

// Usage


document.addEventListener("DOMContentLoaded", function() {
    const replyButtons = document.querySelectorAll(".reply-button");
    
    const loadRepliesButtons = document.querySelectorAll(".load-replies-button");
    
    replyButtons.forEach(button => {
        button.addEventListener("click", function() {
            const replyForm = this.parentElement.querySelector(".reply-form");
            replyForm.style.display = replyForm.style.display === "none" ? "block" : "none";
        });
    });

    loadRepliesButtons.forEach(button => {
        button.addEventListener("click", function() {
            const replies = this.parentElement.querySelector(".replies");
            const replyId = this.getAttribute('data-reply-id');
            console.log(replyId);
            //(fetchData(replyId));
            replies.style.display = replies.style.display === "none" ? "block" : "none";
            
            // Create and insert sample reply elements
            const sampleReplies = [];
            fetchData(replyId).then(data => {
                const replyElement = document.createElement("div");
                replyElement.className = "sample-reply";
                replyElement.innerHTML = `
                    <div class="user-profile"></div>
                    <span class="user-name">${data.username}:</span> ${data.text}`;
            }).catch(error => {
                // Handle any errors 
                console.log(data)
                console.error('An error occurred:', error);
            });
            console.log(sampleReplies)
            sampleReplies.forEach(replyData => {
                console.log(replyData)
                const replyElement = document.createElement("div");
                replyElement.className = "sample-reply";
                replyElement.innerHTML = `
                    <div class="user-profile"></div>
                    <span class="user-name">${replyData.username}:</span> ${replyData.text}`;
                replies.appendChild(replyElement);
            });
            fetchData(replies)
        })
    });
});
*/