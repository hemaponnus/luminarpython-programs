
  #18/3/21-17

          # oops-objected  oriented programs

# class
    # class is a design pattern/blueprint.we can create any no of objects using the pattern,
    # object =real world entity
    # eg: class: TV  ; object :samsung,galaxy

## object

   # real world entity

# reference
    # reference are used to perform operations over object
     # eg ; object:tv ;  refer :remote form vol incre,decre


class Person:
    def walk(self):
        print("person is walking")
    def run(self):
        print("person is running")
    def jumping(self):
        print("person is jumping")
obj=Person()
obj.walk()
obj.run()
obj.jumping()
ab=Person()
ab.walk()
                                   # output

                               #person is walking
                               #person is running
                               #person is jumping
                               #person is walking