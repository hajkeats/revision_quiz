# revision_quiz
Quiz yourself on your revision topic using the terminal!

Within a `<name>.json` file, create a structure like:
```json
    {
        "Topic 1": {
            "Question 1": "Answer 1",
            "Question 2": "Answer 2"
        },
        "Topic 2" : {
	    # ...
    }
```
> Example quiz files exists in `malay.json` and `aws.json`.    

Then run `./quiz.py <name>.json` and quiz yourself!

> Optional Args:
    * Use '--multiple_choice' to create a multiple choice quiz 
    * Use '--reversed' to quiz yourself on the answers rather than the questions
