def getlistclass_BicyclIObetter_Base():
    a = """
    classdiagram BicycleIO {
    /**
    * Light output
    */
    """
    b = """
    public class Light {
      + double lumen;
    }
    """
    c = """
    public enum Breaktype {
      DISK, RIM, DRUM, NONE;
    }
    """
    d = """
    public class Breaks {
      + double wear;
      + double breakingpower;
      + Breaktype type;
    }
    """
    e = """
    public enum Pedal {
      BLOCK, FLAT, RACING, NONE;
    }
    """
    f = """
    public class Sprocket {
      + int teethFront;
      + Pedal pedal_right;
      + Pedal pedal_left; 
    }
    """
    g = """
    /**
    * Gear
    */
    public class GearRatio {
      + double actual_reinforcement;
      + double target_reinforcement;
    }
    """
    h = """
    public class RearWheel {
      + double diamter;
      + Break break;
      + int teethRear;
    }
    """
    i = """
    public class FrontWheel {
      + double diamter;
      + Break break;
    }
    """
    j = """
    public class Dynamo {
      + Electricity electricity_produced;
    }
    """
    k = """
    public class Distance {
      + int meter;
    }
    """
    l = """
    public class Electricity {
      + double volt;
      + double coulomb;
    }
    """
    m = """
    public class Lamp {
      + Electricity in;
      + Light out;
    }    
    """
    n = """
    public class Bike {
    + double speed_m_per_s;
    + Dynamo dynamo;
    + GearRatio current_ratio;
    + Distance coveredDistance;
    + Lamp rearLight;
    + Lamp frontLight;
    }
    """
    o = """
    association [1] Dynamo (produces) <-> (consumes)Lamp [*];
    association [1] GearRatio (Target_teeth) <-> (Actual_teeth) FrontWheel [1];  
    association [1] GearRatio (Target_teeth) <-> (Actual_teeth) RearWheel [1];
    association [*] Breaks (Dynamo_breaking) <- Dynamo [1];
    }
    """
    x = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
    return x

def getlistclass_BicyclIObetter_Structure():
  a ="""
  classdiagram BicycleIO {
  """
  b = """
  public enum Breaktype {
    DISK, RIM, DRUM, NONE;
  }
  """
  c = """
  public class Breaks {
    + double breakingpower;
    + Breaktype type;
  }
  """
  d = """
  public enum Pedal {
    BLOCK, FLAT, RACING, NONE;
  }
  """
  e = """
  /**
   * Gear
   */
  public class GearBox {
    + double actual_reinforcement;
    + double target_reinforcement;
  }
  """
  f = """
  public abstract class Wheel{
    + double diamter;
    + Break break;
    + int teething;  
  } 
  """
  g = """
  public class FrontWheel extends Wheel{
    + Pedal pedal_right;
    + Pedal pedal_left; 
  }
  """
  h = """
  public class RearWheel extends Wheel;
  """
  i = """
  public class Dynamo {
    + Electricity electricity_produced;
  }
  """
  j = """
  public class Tracker {
    + int distance_meter;
    + double current_speed;
  }
  """
  k = """
  public class Electricity {
    + double volt = 120.0;
    + double coulomb;
  }
  """
  l = """
  public class Lamp {
    + Electricity in;
    + double lumen_out;
  }    
  """
  m = """
  public class Bike {
  + double wear;
  + Tracker tracker;
  + Dynamo dynamo;
  + GearBox gearBox;
  + Lamp rearLight;
  + Lamp frontLight;
  }
  """
  n = """
  association [1] Dynamo (produces) <-> (consumes)Lamp [*];
  association [1] GearBox (Target_teeth) <-> (Actual_teeth) FrontWheel [1];  
  association [1] GearBox (Target_teeth) <-> (Actual_teeth) RearWheel [1];
  association [*] Breaks (Dynamo_breaking) <- Dynamo [1];
  }
  """
  x = [a,b,c,d,e,f,g,h,i,j,k,l,m,n]
  return x

def getlistclass_Universitybetter_Base():
  a = """classdiagram University {
  """
  b = """
  interface Person {
    String fullName;
    String address;
    Date dateOfBirth;
  }
  """
  c = """
  abstract class Lecturer implements Person{
    Subject subject;
  }
  """
  d = """
  class Course {
    Subject subject;
    Exam exam;
    Lecture lecture;
    int credits;
  }
  """
  e = """
  class Exam{
    Date first;
    Date second;
    int duration_minutes;
  }
  """
  f = """
  class Lecture {
    List<Date> appointment;
    int total_hours;
  }
  """
  g = """
  class Student implements Person{
    int credits;
    int semester;
    Subject subject;
    Form form;
  }
  """
  h = """
  public enum Form {
    BACHELOR, MASTER, PHD;
  }
  """
  i = """
  package university.staff {
    class Employee extends Person {
      int employeeID;
      int salary;
    }
  """
  j = """
    class Chair{
      String id;
      Subject subject;
      String researchArea;
    }
  """
  k = """
    class Professor extends Lecturer{
      Chair member;
      int ProfessorID;
      String current_research_area;
    }
  """
  l = """
    class Assistant extends Employee{
      Chair member;
      Form form;
    }
  }
  """
  m = """
  association [1] Lecturer (heldBy) <-> (holds) Lecture [*];
  association [1..*] Student <-> (studies) Course [*];
  association [3..*] Employee (Oversees) <-> Exam [*];
  association [1..*] Lecturer (Clarification) <-> Exam [*];
  association [1] Student (Final_thesis) -> Exam [1];
  association [*] Assistant <-> Professor [1];
  }
  """
  x = [a,b,c,d,e,f,g,h,i,j,k,l,m]
  return x

def getlistclass_Universitybetter_Structure():
  a = """
  classdiagram University {
  """
  b = """
  abstract class Person {
    String fullName;
    String address;
    Date dateOfBirth;
  }
  """
  c = """
  class Lecture {
    List<Date> appointment;
    int total_hours;
  }
  """
  d = """
  class Student extends Person{
    int credits;
    int semester;
    Subject subject;
    Form form;
  }
  """
  e = """
  class Course {
    Subject subject;
    Date first_exam;
    Date second_exam;
    int exam_duration_minutes;
    Lecture lecture;
    int credits;
  }
  """
  f = """
  public enum Form {
    BACHELOR, MASTER, PHD;
  }
  """
  g = """
    class Employee extends Person {
      int employeeID;
      int salary;
    }
  """
  h = """
    class Chair{
      String id;
      Subject subject;
      String researchArea;
    }
  """
  i = """
    class Professor{
      Subject subject;
      int ProfessorID;
      String current_research_area;
    }
  """
  j = """
    class Assistant extends Employee{
      Form form;
    }
  """
  k = """
  association [1] Professor (heldBy) <-> (holds) Lecture [*];
  association [1..*] Student <-> (studies) Course [*];
  association [3..*] Employee (Oversees) <-> Exam [*];
  association [1..*] Professor (Clarification) <-> Exam [*];
  association [1] Student (Final_thesis) -> Exam [1];
  association [*] Assistant <-> Professor [1];
  association [1..*] Professor (member) <-> Chair [*];
  association [*] Assistant (employed) <-> Chair [1];
  } """
  x = [a,b,c,d,e,f,g,h,i,j,k]
  return x

def getlistclass_BicycleIO_Base():
  a = """
  classdiagram BicycleIO {
  """
  b = """
  /**
   * Kinetic energy measured as joule.
   */
  public class Energy {
    + double joule;
  }
  """
  c = """
  /**
   * Light output
   */
  public class Light {
    + double lumen;
  }
  """
  d = """
  /**
   * Gear
   */
  public class GearRatio {
    + int teethFront;
    + int teethRear;
  }
  """
  e = """
  /**
   * measured rotation in radian
   */
  public class Rotation {
    + double radian;
  }
  """
  f = """
  public class Crankset {
  }
  """
  g = """
  public class Sprocket {
  }
  """
  h = """
  public class RearWheel {
  }
  """
  i = """
  public class FrontWheel {
  }
  """
  j = """
    public class Dynamo {
      Electricity electricity;
  }
  """
  k = """
  public class Distance {
    + double meter;
  }
  """
  l = """
  public class Electricity {
    + double volt;
    + double coulomb;
  }
  """
  m = """
  public class Lamp {
    + Electricity in;
    + Light out;
  }    
  """
  n = """
  public class Bike {
  + Energy energy;
  + GearRatio ratio;
  + Distance coveredDistance;
  + Light rearLight;
  + Light frontLight;
  }
  """
  o = """
  }
  """
  x = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
  return x

def getlistclass_BicycleIO_Structure():
  a = """
  classdiagram BicycleIO {
  /**
   * Kinetic energy measured as joule.
   */
  """
  b = """
  public class Energy {
    + double joule;
  }
  """
  c = """
  /**
   * Light output
   */
  public class Light {
    + double lumen;
  }
  """
  d = """
  /**
   * measured rotation in radian
   */
  public class Rotation {
    + double radian;
  }
  """
  e = """
  public class Lamp {
    + Energy usable_Energy;
    + Light out_front;
    + Light out_rear;
  }    
  """
  f = """
  public class Bike {
  + Energy energy;
  + int teethFront;
  + int teethRear;
  + double meter_coveredDistance;
  + Lamp lamp;
  }
  """
  g = """
  }
  """
  x = [a,b,c,d,e,f,g]
  return x

def getlistclass_University_Base():
  a = """
  classdiagram University {
  
  public interface Lecturer;
  """
  b = """
  abstract class Person {
    public String fullName;
    String address;
    Date dateOfBirth;
  }
  """
  c = """
  class Course {
    Subject subject;
  }
  """
  d = """
  class Lecture {
    int credits;
  }
  """
  e = """
    class Employee extends Person {
      int employeeID;
    }
  """
  f = """
    class Professor extends Person implements Lecturer;
    class Chair{
      String id;
      String researchArea;
  }
  """
  g = """
  association [1] Lecturer (heldBy) < - > (holds) Lecture;
  association Student (attendees) < - > (attends) Lecture;
  association [*] Course - > (curriculum) Lecture [1..*];
  association [1..*] Student < - > (studies) Course [1..*];
  }
  """
  x = [a,b,c,d,e,f,g]
  return x

def getlistclass_University_Structure():
  a = """
  classdiagram University {
  """
  b = """
    public interface Lecturer;
    abstract class Person
  """
  c = """
    class Employee extends Person {
      int employeeID;
      public String fullName;
      String address;
      Date dateOfBirth;
    }
  """
  d = """
    class Professor extends Employee implements Lecturer;
  """
  e = """
    class Chair{
      String id;
      String researchArea;
  }
  """
  f = """
  class Course {
    Subject subject;
  }
  """
  g = """
  class Lecture {
    int credits;
    Lecturer teacher;
  }
  """
  h = """
  association Student (attendees) < - > (attends) Lecture;
  association [*] Course - > (curriculum) Lecture [1..*];
  association [1..*] Student < - > (studies) Course [1..*];
  }
  """
  x = [a,b,c,d,e,f,g,h]
  return x
