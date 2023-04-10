from django.db import models

# Voting question
class Question(models.Model):
    """Class containing the database question table with fields for the question and
      date published for each of the polls

    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

def _str_(self):
        """This method will return the relevant question detail from the question record

        :returns: The question detail from the record 

        :rtype: str
        """
        return self.question_text
    
# Selection for votes
class Choice(models.Model):
    """
    Class containing vote table with vote options and tallies linked to each question by
      foreign key
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

def _str_(self):
        """This method will return the choices available for each question record
        
        :returns: Each choice linked to a question

        :rtype: str
        """
        return self.choice_text


