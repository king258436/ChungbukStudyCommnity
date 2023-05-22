document.addEventListener("DOMContentLoaded", function(){
    let popular_post_element = document.getElementById('popular-post')
    let popular_post_html = ""
    
    for (let i = 0; i < 6; i++) {
        popular_post_html += `
    <a class="list" href="#">
        <p class="hot_logo">hot</p>
        <p class="post-title">게시물 제목 ${i}</p>
        <p class="subject_name">과목(게시판) 이름</p>
    
        <p class="vote active">10(따봉)</p>
        <p class="comment active">10(댓글수)</p>
    
        <p>xx:xx</p>
        <hr>
    </a>
    `
    }
    
    console.log(popular_post_element)
    popular_post_element.innerHTML = popular_post_html
});