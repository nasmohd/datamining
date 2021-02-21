import scrapy



class QuotesSpider(scrapy.Spider):
	name = "students"
	start_urls = [
		'https://nasmohd.github.io/osim.github.io/'
	]

	
	def parse(self, response):
		total_students = response.css ("div.cboxElement span.filename::text").getall()  #Get all student entries
		students = []

		i = 2
		p = 0
		while (i <= len(total_students)):
			student_ent = response.css ("div.cboxElement span.filename::text")[i].get()
			regNo = response.css ("div.cboxElement span.filename::text")[i-1].get()

			#Customize the regNo to look as we want by removing some characters
			regNo = regNo.replace ('\n                            ', '')
			regNo = regNo.replace ('-', '')

			session_det = response.css ("div.cboxElement div::text")[p].get()
			session_det = session_det.replace ('\n                            ', '')
			session_det = session_det.replace ('                                                       ', '')


			yield {
				'Name': response.css ("div.cboxElement span.filename::text")[i].get(),
				'RegNo': regNo,
				'Session': session_det
			}

			students.append(student_ent)
			i = i + 3
			p = p + 4





#From Shell Testing
#response.css ("div.cboxElement span.filename::text")[1].get() returns '\n 1802393933818'

#response.css ("div.cboxElement span.filename span::text")[0].get() returns '1'
#response.css ("div.cboxElement span.filename span::text")[1].get() returns 'Female'
#response.css ("div.cboxElement span.filename span::text")[2].get() returns 'Student Name here'

#response.css ("div.cboxElement span.filename::text")[2].get() returns "Student Name"

#response.css ("div.cboxElement span.filename::text")[1].get() returns "\n 1802393933818"



#response.css ("div.cboxElement span.filename::text").getall()
#response.css ("div.cboxElement div::text").getall() returns sessions 0, 4, 8, 12