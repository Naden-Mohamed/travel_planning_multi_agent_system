from pydantic import BaseModel, Field
from typing import List


class Place(BaseModel):
    name: str = Field(
        ...,
        description="Name of the recommended place or activity, e.g. 'Valley of the Kings'."
    )
    description: str = Field(
        ...,
        description="One-line description of the place and why it fits the traveler's stated interests."
    )


class Category(BaseModel):
    category: str = Field(
        ...,
        description="Category label grouping these places, e.g. 'Cultural Experiences', 'Culinary Adventures'."
    )
    places: List[Place] = Field(
        ...,
        min_length=1,
        description="Places/activities belonging to this category."
    )


class DestinationRecommendations(BaseModel):
    destination: str = Field(
        ...,
        description="The destination that was researched."
    )
    categories: List[Category] = Field(
        ...,
        min_length=1,
        description="Recommended places grouped by category. Should total 6-10 places across all categories combined."
    )
 
class DayTime(BaseModel):
    morning: str = Field(
        ...,
        description="The activity recommendation for the morning, written as a short narrative sentence."
    )
    afternoon: str = Field(
        ...,
        description="The activity recommendation for the afternoon, written as a short narrative sentence."
    )
    evening: str = Field(
        ...,
        description="The activity recommendation for the evening, written as a short narrative sentence."
    )
 
 
class DayPlan(BaseModel):
    day_num: int = Field(
        ...,
        description="The number of the day in the trip, e.g. 1, 2, 3."
    )
    day_title: str = Field(
        ...,
        description=(
            "A short, evocative theme title summarizing the day's plan, "
            "e.g. 'Imperial Roots and Roman Flavors'. Rendered as the bolded "
            "heading for the day."
        )
    )
    schedule: DayTime = Field(
        ...,
        description="The single morning/afternoon/evening schedule for this day."
    )
 
 
class Itinerary(BaseModel):
    num_trip_days: int = Field(
        ...,
        description="The user-defined total number of trip days."
    )
    days_plan: List[DayPlan] = Field(
        ...,
        description="The full day-by-day plan, one DayPlan entry per day, in order."
    )
 