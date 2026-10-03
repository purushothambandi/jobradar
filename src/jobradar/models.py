from dataclasses import dataclass,field
@dataclass
class Job:
    id:str
    title:str
    company:str
    location:str
    description:str
    url:str
    skills:list[str] = field(default_factory=list)
    def __post_init__(self):
        self.title=self.title.strip()
        self.company=self.company.strip()



