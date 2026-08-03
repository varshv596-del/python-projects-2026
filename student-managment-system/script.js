const form = document.getElementById("studentForm");
const studentList = document.getElementById("studentList");

let students = JSON.parse(localStorage.getItem("students")) || [];

displayStudents();

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const course = document.getElementById("course").value;

    const student = {
        name,
        age,
        course
    };

    students.push(student);

    localStorage.setItem("students", JSON.stringify(students));

    displayStudents();

    form.reset();
});

function displayStudents() {
    studentList.innerHTML = "";

    students.forEach((student, index) => {
        studentList.innerHTML += `
            <div class="student">
                <h3>${student.name}</h3>
                <p><strong>Age:</strong> ${student.age}</p>
                <p><strong>Course:</strong> ${student.course}</p>

                <button class="deleteBtn" onclick="deleteStudent(${index})">
                    Delete
                </button>
            </div>
        `;
    });
}

function deleteStudent(index) {
    students.splice(index, 1);

    localStorage.setItem("students", JSON.stringify(students));

    displayStudents();
}const searchStudent = document.getElementById("searchStudent");

searchStudent.addEventListener("keyup", function () {
    const value = searchStudent.value.toLowerCase();

    const students = document.querySelectorAll(".student");

    students.forEach(function (student) {
        const text = student.innerText.toLowerCase();

        if (text.includes(value)) {
            student.style.display = "block";
        } else {
            student.style.display = "none";
        }
    });
});