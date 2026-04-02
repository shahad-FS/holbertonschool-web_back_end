function updateStudentGradeByCity(students, city, newGrades) {
	if (!Array.isArray(students)) {
		return [];
	}
	if (!Array.isArray(newGrades)){
		return [];
	}

	const stdCity = students.filter((student) => student.location === city);
	const studentsGrade = stdCity.map((student) => {
		const gradeFilter = newGrades.filter(
			(newGrade) => newGrade.sudentId === student.id);
		let grade;

		if (gradeFilter[0]) {
			grade = gradeFilter[0].grade;
		} else {
			grade = 'N/A';
		}

		return {
			...student,
			grade,
		};
	});

	return studentsGrade;
	}

export default updateStudentGradeByCity;
